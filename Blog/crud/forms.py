from django import forms  
from crud.models import Post

class BlogForm(forms.ModelForm):  
    class Meta:  
        model = Post  
        fields = ['title','author','content','status','created_on']
        

