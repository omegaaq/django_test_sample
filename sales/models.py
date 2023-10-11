from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} : {self.surname} : {self.phone} : {self.email}"

class Salesman(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    employment_date = models.DateField()
    position = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} : {self.surname} : {self.phone} : {self.email} : {self.employment_date} : {self.position}"

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} : {self.description}"

class Sales(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, related_name="sales")
    salesman = models.ForeignKey(Salesman, on_delete=models.RESTRICT, related_name="sales")
    product = models.ManyToManyField(Product, related_name="sales")
    sales_date = models.DateTimeField()
    cash_amount = models.FloatField()

    def __str__(self):
        return f"{self.client} : {self.salesman} : {self.sales_date} : {self.cash_amount}"