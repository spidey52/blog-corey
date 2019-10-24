from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering= ('-date_posted',)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # messages.success(f'your blog is succesfully created ')
        return reverse('post-detail', kwargs={'pk': self.pk })
        