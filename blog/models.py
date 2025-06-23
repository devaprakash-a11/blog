from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='post_images/', blank=True, null=True) 

    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
