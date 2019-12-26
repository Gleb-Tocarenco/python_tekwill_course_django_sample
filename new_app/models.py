from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    date_published = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blog Posts'


