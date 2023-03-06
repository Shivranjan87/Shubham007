from django.contrib import admin

# Register your models here.

from Customer.models import customer
from Customer.models import customer_new
from Customer.models import Product
from Customer.models import Booking
#
# class customerAdmin(admin.ModelAdmin):
#     list_display = ( 'fname','lname','location','state')

admin.site.register(customer)
admin.site.register(customer_new)
admin.site.register(Product)
admin.site.register(Booking)





