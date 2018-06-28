from django.shortcuts import render

# Create your views here.
def posts(request):
    context = {
        'message': 'hello'
    }
    return render(request, 'posts.html', context)
