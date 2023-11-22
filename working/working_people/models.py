from django.db import models

class WorkingProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    address = models.CharField(max_length=250, verbose_name="Address")
    email = models.EmailField(max_length=250, verbose_name="Email")
    profile_photo = models.ImageField(upload_to="profile-photos/", verbose_name="Profile-photos")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    price = models.FloatField(null=False)

