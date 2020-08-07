from django.db import models

class cart_items(models.Model):
    name = models.TextField()
    price = models.TextField()
    img = models.TextField()
    
