from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, ProfileForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .forms import PostForm

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # ✅ Only owner can edit
    if post.author != request.user:
        messages.error(request, "You are not allowed to edit this post.")
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {
        'form': form,
        'post': post
    })


def profile(request, username):
    user_profile = get_object_or_404(User, username=username)

    posts = Post.objects.filter(author=user_profile).order_by('-created_at')

    return render(request, 'blog/profile.html', {
        'profile_user': user_profile,
        'posts': posts
    })

def home(request):
    query = request.GET.get("q", "")
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).order_by("-created_at")

    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, "blog/home.html", {"posts": posts})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully")
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(request.META.get("HTTP_REFERER", "/"))


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                messages.success(request, "Comment added")
                return redirect("post_detail", post_id=post.id)
        else:
            messages.error(request, "Login required")

    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })


@login_required
def profile_view(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, "blog/profile.html", {"profile": profile})


@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated")
            return redirect("profile", request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, "blog/edit_profile.html", {"form": form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        post.delete()

    return redirect('home')
