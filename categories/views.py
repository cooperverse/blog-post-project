from django.shortcuts import render, redirect
from categories.forms import AddCategory
def add_category(request):
    if request.method == "POST":
        add_category = AddCategory(request.POST)
        if add_category.is_valid():
            add_category.save()
            return redirect('add_category')
    else:
        add_category = AddCategory()
    
    return render(request, 'category.html',{"add_category":add_category})
            