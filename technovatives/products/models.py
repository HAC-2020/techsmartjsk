from django.db import models

class products(models.Model):
    name = models.TextField()
    price = models.TextField()
    img = models.TextField()
