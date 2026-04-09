from django.db import models

class Home(models.Model):
    title=models.CharField(max_length=200, help_text="title", verbose_name="title")
    text=models.TextField(help_text="text", verbose_name="desciption")
    img=models.ImageField(upload_to="home")

    def __str__(self):
        return self.title

class About(models.Model):
    title1=models.CharField(max_length=200, verbose_name="title")
    title2 = models.CharField(max_length=200, verbose_name="title")
    text1=models.TextField(verbose_name="text1")
    text2 = models.TextField(verbose_name="text2")
    text3 = models.TextField(verbose_name="text3")
    img1 = models.ImageField(upload_to="home", verbose_name="img")
    img2 = models.ImageField(upload_to="home", verbose_name="img")
    img3 = models.ImageField(upload_to="home", verbose_name="img")


    def __str__(self):
        return self.title1

# Create your models here.
