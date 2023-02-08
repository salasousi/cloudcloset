from django.db import models

# Create your models here.
class Top(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Bottom(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Coat(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Shoe(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Accessory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category