import markdown
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_markdown(self):
        return mark_safe(
            markdown.markdown(self.content, extensions=["fenced_code", "codehilite"])
        )
