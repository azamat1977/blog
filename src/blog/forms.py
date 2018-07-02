from blog.models import Article, Category
from django import forms


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = []
        
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []
