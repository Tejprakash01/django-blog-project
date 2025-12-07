from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post


@login_required
def home(request):
    posts = Post.objects.all().order_by('-created')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            image=request.FILES.get("image")
        )
        return redirect('home')

    return render(request, 'blog/create_post.html')
