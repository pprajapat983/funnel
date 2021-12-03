from django.db import models

# Create your models here.
class Customer(models.Model):
    cust_id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=300)


    def __str__(self):
        return self.email