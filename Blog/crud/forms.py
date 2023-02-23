from django import forms  
from crud.models import Post

class BlogForm(forms.ModelForm):  
    # title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'title','class':'form-control'}))
    # author=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'author','class':'form-control'}))
    # content=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'content','class':'form-control'}))
    # status=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'status','class':'form-control'}))
    # created_on=forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder':'date','class':'form-control'}))


    class Meta:  
        model = Post  
        fields = ['title','author','content','status','created_on']
       
        widgets={

             'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'title'
                }),

                'author': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'author'
                }),

                'content': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'content'
                }),

                'status': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'status'
                }),

                'created_on': forms.DateTimeInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'date'
                }),
        }
        

