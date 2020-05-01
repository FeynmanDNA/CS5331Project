from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = [
            'title',
            'title_color',
            'body',
            'slug',
            'thumb',
            'imgSize',
            'author_homepage',
            # new contexts for xss:
            'iframe_src',
            'formaction',
            'math_href',
        ]
