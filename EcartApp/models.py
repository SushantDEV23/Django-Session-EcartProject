from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=90)
    price=models.FloatField()
    description=models.CharField(max_length=150)
    image_url=models.CharField(max_length=100)
