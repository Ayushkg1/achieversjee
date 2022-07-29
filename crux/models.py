from django.db import models

# Create your models here.


class Chapter(models.Model):
    chapter_id = models.BigAutoField(primary_key=True)
    chapter_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    chapter_desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images', default="")
    yt_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")

    def __str__(self):
        return self.chapter_name


class Material(models.Model):
    material_id = models.BigAutoField(primary_key=True)
    main_heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=50)
    link_specifier_1 = models.CharField(max_length=50,default="")
    first_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")
    link_specifier_2 = models.CharField(max_length=50,default="")
    second_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")

class Mathematics(models.Model):
    maths_id = models.BigAutoField(primary_key=True)
    main_heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=50)
    link_specifier_1 = models.CharField(max_length=50,default="")
    first_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")
    link_specifier_2 = models.CharField(max_length=50,default="")
    second_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")

class Physics(models.Model):
    physics_id = models.BigAutoField(primary_key=True)
    main_heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=50)
    link_specifier_1 = models.CharField(max_length=50,default="")
    first_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")
    link_specifier_2 = models.CharField(max_length=50,default="")
    second_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")

class Chemistry(models.Model):
    chemistry_id = models.BigAutoField(primary_key=True)
    main_heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=50)
    link_specifier_1 = models.CharField(max_length=50,default="")
    first_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")
    link_specifier_2 = models.CharField(max_length=50,default="")
    second_link = models.URLField(
        max_length=150, default="https://www.youtube.com/c/AnjeshNITJ")


class Contact(models.Model):
    contact_id = models.BigAutoField(primary_key=True)
    contact_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    contact_desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.contact_name
