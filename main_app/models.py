from django.db import models
from django.urls import reverse

# Create your models here.
class Toptype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toptype_detail', kwargs={'pk': self.id})


class Top(models.Model):
    category = models.CharField(max_length=100)
    toptypes = models.ManyToManyField(Toptype)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("t_detail", kwargs={'top_id': self.id})


class Bottomtype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bottomtype_detail', kwargs={'pk': self.id})


class Bottom(models.Model):
    category = models.CharField(max_length=100)
    bottomtypes = models.ManyToManyField(Bottomtype)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("b_detail", kwargs={'bottom_id': self.id})


class Coattype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coattype_detail', kwargs={'pk': self.id})


class Coat(models.Model):
    category = models.CharField(max_length=100)
    coattypes = models.ManyToManyField(Coattype)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("c_detail", kwargs={'coat_id': self.id})


class Shoetype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shoetype_detail', kwargs={'pk': self.id})


class Shoe(models.Model):
    category = models.CharField(max_length=100)
    shoetypes = models.ManyToManyField(Shoetype)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("s_detail", kwargs={'shoe_id': self.id})


class Accessorytype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessorytype_detail', kwargs={'pk': self.id})


class Accessory(models.Model):
    category = models.CharField(max_length=100)
    accessorytypes = models.ManyToManyField(Accessorytype)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("a_detail", kwargs={'accessory_id': self.id})
