from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=150)

    def __str__(self):
        return self.nom



class Yangiliklar(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    sarlavha = models.CharField(max_length=250)
    sl_url = models.SlugField(max_length=250)
    matn = models.TextField()       
    rasm = models.ImageField(upload_to='yangiliklar/rasm')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft,
                              )


    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.sarlavha

    def get_absolute_url(self):
        return reverse("yangilik_detail", args=[self.sl_url])


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name



