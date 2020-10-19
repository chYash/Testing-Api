from django.db import models


class Bug(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name

class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneno = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
class Expense(models.Model):

    title = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField()
    user = models.ForeignKey('User',on_delete=models.PROTECT,null=True,blank=True)
    income = models.PositiveIntegerField()
    expense = models.PositiveIntegerField()

    def __str__(self):
        return str(self.date)

