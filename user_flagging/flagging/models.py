from django.db import models
#from django.core.validators import MinLengthValidator

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11)
    
    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"

class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Flag(models.Model): 
    Date = models.DateField()
    Message = models.CharField(max_length=200, blank=True)
    Customer = models.ManyToManyField("Customer", related_name="flags")
    businesses = models.ManyToManyField("Business", related_name="users")

    def __str__(self):
        return f"{self.id}: {self.Date}"
