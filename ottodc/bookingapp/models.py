from django.db import models


class Dealer(models.Model):
    Name = models.TextField(null=False)
    Place = models.TextField(null=False)
    Email = models.TextField(null=True)
    GST = models.TextField(null=True)
    Phone = models.TextField(null=True)
    Site_code = models.IntegerField(null=False)

    def __str__(self):
        return self.Name


class Category(models.Model):
    Name = models.TextField(null=False)

    def __str__(self):
        return self.Name


class Brand(models.Model):
    Name = models.TextField(null=False)
    Categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.Name

