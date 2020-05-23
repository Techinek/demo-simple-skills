from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title
