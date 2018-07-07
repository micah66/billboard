from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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


@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        else:
            print('ERROR!')
        return HttpResponseRedirect(reverse('posts'))
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'billboard/registration.html', context)
