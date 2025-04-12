from django.shortcuts import render

from blog.models import Post


def home(request):
    posts = Post.objects.order_by("-created_at")[:5]
    return render(request, "home.html", {"posts": posts})
