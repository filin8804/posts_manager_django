from datetime import datetime
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
class Post(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, unique=False)