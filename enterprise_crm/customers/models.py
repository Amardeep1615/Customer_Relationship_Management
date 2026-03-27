from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    create_at = models.DateTimeField(max_length = 20)
