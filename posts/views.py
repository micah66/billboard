from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.
@csrf_protect
def posts(request):
    posts = Post.objects.all()
    date = timezone.now()
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            Post.objects.create(**post.cleaned_data)
        return redirect('/posts/')
    else:
        post = PostForm()
    context = {
        'post': post,
        'posts': posts,
        'date': date
    }
    return render(request, 'billboard/posts.html', context)
