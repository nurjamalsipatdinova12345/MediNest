from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    icon = models.CharField(max_length=50, help_text="example: fas fa-heartbeat", verbose_name="icon")
    img=models.ImageField(upload_to='departments/', verbose_name="photo")
    description = models.TextField(verbose_name="decription")
    def __str__(self):
        return self.name
class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors', verbose_name="Department")
    specialty = models.CharField(max_length=100, verbose_name="specialty")
    image = models.ImageField(upload_to='doctors/', verbose_name="photo")
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name
class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name="title")
    description = models.TextField(verbose_name="description")
    icon = models.CharField(max_length=50, help_text="example: bi bi-capsule", verbose_name="icon")
    image = models.ImageField(upload_to='services/', verbose_name="photo")
    def __str__(self):
        return self.title

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    def __str__(self):
        return self.name

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
