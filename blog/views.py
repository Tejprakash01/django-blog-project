from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, ProfileForm, RegisterForm


def home(request):
    q = request.GET.get("q", "")
    posts = Post.objects.filter(
        Q(title__icontains=q) | Q(content__icontains=q)
    ).order_by("-created_at")

    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, "blog/home.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm()
    return render(request, "blog/post_detail.html", {
        "post": post,
        "form": form
    })


@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("home")
    return render(request, "blog/create_post.html", {"form": form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "blog/edit_post.html", {"form": form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    post.delete()
    return redirect("home")


@login_required
def like_post_ajax(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True

        return JsonResponse({
            "liked": liked,
            "likes_count": post.likes.count()
        })



@login_required
def add_comment_ajax(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

        return JsonResponse({
            "id": comment.id,
            "user": comment.user.username,
            "text": comment.text
        })
    return JsonResponse({"error": "Invalid"}, status=400)

@login_required
def delete_comment_ajax(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    comment.delete()
    return JsonResponse({"success": True})



def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, "blog/profile.html", {
        "profile_user": user,
        "posts": posts
    })


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})
