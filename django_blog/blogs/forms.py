from django import forms
from blogs.models import Post,Comment,Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
  

class PostForm(forms.ModelForm):  
    class Meta:  
        model = Post
        fields = ['title','content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5,'placeholder':'Content Here ... '}),   
            'title': forms.TextInput(attrs={'class' : 'form-control','placeholder':'Title ... '})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']  
        widgets = {
            'comment': forms.TextInput(attrs={'class' : 'form-control','placeholder':'Comment Here ... '})
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']
        widgets = {
            'tag': forms.TextInput(attrs={'class' : 'form-control','placeholder':'tag1,tag2,tag3,...'})
        }
        help_texts = {
            'tag': ("Tags are to be comma(',') seperated"),
        }
 

              
