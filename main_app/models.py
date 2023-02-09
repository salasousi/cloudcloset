from django.db import models
from django.urls import reverse

# Create your models here.
# class Toptype(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('toptype_detail', kwargs={'pk': self.id})


class Top(models.Model):
    category = models.CharField(max_length=100)
    # toptypes = models.ManyToManyField(Toptype)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("t_detail", kwargs={'top_id': self.id})


class Bottom(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("b_detail", kwargs={'bottom_id': self.id})


class Coat(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("c_detail", kwargs={'coat_id': self.id})


class Shoe(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("s_detail", kwargs={'shoe_id': self.id})


class Accessory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("a_detail", kwargs={'accessory_id': self.id})


class Topphoto(models.Model):
    url = models.CharField(max_length=200)
    top = models.ForeignKey(Top, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for top_id: {self.top_id} @{self.url}"

class Bottomphoto(models.Model):
    url = models.CharField(max_length=200)
    bottom = models.ForeignKey(Bottom, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for bottom_id: {self.bottom_id} @{self.url}"

class Coatphoto(models.Model):
    url = models.CharField(max_length=200)
    coat = models.ForeignKey(Coat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for coat_id: {self.coat_id} @{self.url}"

class Shoephoto(models.Model):
    url = models.CharField(max_length=200)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for shoe_id: {self.shoe_id} @{self.url}"

class Accessoryphoto(models.Model):
    url = models.CharField(max_length=200)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for accessory_id: {self.accessory_id} @{self.url}"
