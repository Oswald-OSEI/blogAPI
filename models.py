from django.db import models

# Create your models here.
class Blog(models.Model):
    Title=  models.CharField(max_length = 200)
    Content = models.TextField()
    Images = models.ImageField(upload_to = 'Blog/Images')
    Date_Uploaded = models.DateTimeField(auto_now_add=True)
    Upload_by = models.CharField(max_length = 100)

    def __str__(self):
        return self.Title