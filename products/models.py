# class product(models.Model):
#     # ফিল্ডসমূহ
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)





from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField (max_length=50)
    describe = models.CharField (max_length=150)
    price = models.CharField (max_length=4)
    def __str__(self):
        return self.title