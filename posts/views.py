from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Post


# Create your views here.
def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'billboard/posts.html', context)
