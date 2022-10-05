from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
 

class Post(models.Model):
    # adding fields
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # default = timezone.now : It wil update the time whenever a new post is created.
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # This is a multirelationship, Post model and User model both have the same table. User
    # One User can have multiple Posts , But multiple posts can have have on;y author.
    # on_delete = models.CASCADE :  When a Post is deleted , it will not delete the user.

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})