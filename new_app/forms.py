from django.forms import ModelForm, ValidationError
from new_app.models import BlogPost


class BlogPostForm(ModelForm):

    def clean_title(self):
        if 'web' in self.cleaned_data['title'].lower():
            raise ValidationError('Web articles cannot be added')
        return self.cleaned_data['title']


    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'author')