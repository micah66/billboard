from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.
@csrf_protect
def posts(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            Post.objects.create(**post.cleaned_data)
    else:
        post = PostForm()
    date = timezone.now()
    context = {
        'post': post,
        'posts': posts,
        'date': date
    }
    return render(request, 'billboard/posts.html', context)
