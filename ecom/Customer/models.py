from django.db import models

# Create your models here.


class customer(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    # contact = models.IntegerField()
    # adhar_no = models.TextField(max_length=200)
    # pan_no = models.TextField(max_length=200)
    # a1 = customer(id=100,fname='mahesh4',lname='gaikwad4',email='ggg@gamil.com',location='pune4',state='MP')

    # def __str__(self):
    #     return (self.fname)




class customer_new(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contact = models.IntegerField()
    adhar_no = models.TextField(max_length=200)
    pan_no = models.TextField(max_length=200)

class Product(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    qty = models.IntegerField()
    contact = models.IntegerField()
    title = models.CharField(max_length=50)
    review = models.TextField()
    user_gender = models.CharField(max_length=100, choices=[('M', 'Male'), ('F', 'Female')])

class Booking(models.Model):

   time = models.TimeField(auto_now=False, auto_now_add=False)
   name = models.CharField(max_length=100)
   people = models.IntegerField()
   info = models.TextField()
   tel = models.CharField(max_length=12)
   date = models.DateField()
   initials = models.CharField(max_length=20)
   created_date = models.DateTimeField(auto_now_add=True)
   table = models.IntegerField(default=0)






