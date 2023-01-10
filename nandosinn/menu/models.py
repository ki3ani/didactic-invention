from django.db import models

# Create your models here

class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class MenuItems(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title
