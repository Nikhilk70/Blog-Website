from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author','title','text',)
        
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control select-combo'}),
            'title': forms.TextInput(attrs={'class': 'textinputclass form_control'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent form-control', 'rows':'3','cols': '80','style': 'width:100%; height:300px;'}),
        }
        

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }