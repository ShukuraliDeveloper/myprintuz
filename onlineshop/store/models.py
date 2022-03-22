from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="static/image")
    price = models.BigIntegerField(verbose_name="start_price")
    stars = models.PositiveIntegerField(null=True)
    tag = models.ManyToManyField(Tag, related_name='product', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='product', null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(null=True)

    @property
    def total_sum(self):
        total = self.quantity * self.product.price
        return total
