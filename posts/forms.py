from django import forms 
from posts.models import Post, Comments

class PostForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    class Meta:
        model = Post
        exclude =['author']
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your comment here...'}), required=False)
    class Meta:
        model = Comments
        fields = ['comment']
        