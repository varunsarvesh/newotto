from django.contrib import admin

# Register your models here.
from bookingapp.models import Brand, Category, Dealer

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Dealer)