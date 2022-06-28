from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    #to be redirected to detail page after creating a post
    def get_absolute_url(self):
        #take care "post-detail is a function  in reverse not the name of your template 'post_detail'"
        #it's confusing when it's string ...but this how it works 
        #django.urls.exceptions.NoReverseMatch: Reverse for 'post_detail' not found. 'post_detail' is not a valid view function or pattern name.
        return reverse("post-detail", kwargs={"pk": self.pk})

