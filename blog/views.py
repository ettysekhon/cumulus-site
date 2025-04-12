from django.shortcuts import get_object_or_404, render

from .models import Post


def blog_index(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "index.html", {"posts": posts})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "detail.html", {"post": post})
