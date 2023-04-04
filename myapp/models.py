from django.db import models

# Create your models here.
class Feature:
    def __init__(self, intro, content, photo = None):
        self.intro = intro
        self.content = content
        self.photo = photo

class Form(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    pesan = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.nama