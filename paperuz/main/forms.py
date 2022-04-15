from .models import Comment, Product
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'phone', 'text')
