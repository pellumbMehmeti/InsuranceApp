from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    surname = models.CharField(max_length = 50, blank = False)
    email = models.CharField(max_length= 20,blank = False)
    username = models.CharField(max_length = 15, blank = False)
    birthday = models.DateTimeField()
    photo = models.URLField(blank=False)  #te verifikohet edhe njihere
    address = models.CharField(max_length = 50, blank = False)
    password = models.CharField(max_length = 15, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ('created_at',)

