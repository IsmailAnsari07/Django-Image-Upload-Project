from django.db import models

# Create your models here.

class Profile_User(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    technology = models.CharField(max_length=500)
    email = models.EmailField(default=None)
    display_picture = models.FileField()


    def __str__(self):
        return self.fname

