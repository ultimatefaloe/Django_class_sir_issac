from django.shortcuts import render

from .models import Post

# Create your views here.
def posts_list(request):
    post  = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': post})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = { 'post': post }
    return render(request, 'posts/post_detail.html', context)