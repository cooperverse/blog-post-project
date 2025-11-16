from django.shortcuts import render
from posts.models import Post
from categories.models import Category
from django.contrib.auth.decorators import login_required
@login_required
def home(request, category_slug=None):
    post = Post.objects.all()
    categories = Category.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        post = Post.objects.filter(category = category)
    
    
    return render(request, 'home.html', {"post":post, "categories":categories})
def front_page(request):
    return render(request, 'front_page.html')