from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from posts.forms import PostForm, CommentForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
# Create your views here.
# @login_required
# def add_post(request):
#     if request.method =='POST': 
#         add_post = PostForm(request.POST)
#         if add_post.is_valid():
#             add_post.instance.author =request.user
#             add_post.save()
#             return redirect("home")
#     else:
#         add_post = PostForm()
    
#     return render(request,'add_post.html', {'add_post': add_post})
# Class Base View Add Post
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required
# def edit_post(request,id):
#     post = Post.objects.get(pk=id)
#     if request.method =='POST': 
#         add_post = PostForm(request.POST, instance=post)
#         if add_post.is_valid():
#             add_post.instance.author = request.user
#             add_post.save()
#             return redirect("my_blogs")
#     else:
#         add_post = PostForm(instance = post)
#     return render(request,'add_post.html', {'add_post': add_post})

# Class Base View Edit Post 
@method_decorator(login_required, name='dispatch')
class EditPostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html" 
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
# @login_required            
# def delete_post(request,id):
#     post = Post.objects.get(pk=id)
#     post.delete()
#     return redirect("my_blogs")

# Class Base View Add Post
@method_decorator(login_required, name='dispatch')
class DeletePostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = "delete_post.html" 
    success_url = reverse_lazy('home')
@method_decorator(login_required, name='dispatch')   
class DetailPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = "detail_post.html" 
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.email = request.user.email
            new_comment.save()
            return redirect('detail_post', id =post.id)
        else:
            comment_form = CommentForm()
        return self.get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form 
        
        return context
        
