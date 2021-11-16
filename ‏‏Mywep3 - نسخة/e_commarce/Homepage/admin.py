from django.contrib import admin
from .models import Country, addtocarts2, cart, cartorder
from .models import Productmen,Users
from .models import addtocarts
#from django.contrib.auth import get_user_model
import os
#Users=get_user_model()
# Register your models here.
admin.site.register(Country)
admin.site.register(Users)
admin.site.register(Productmen)
admin.site.register(addtocarts)
admin.site.register(cart)
admin.site.register(cartorder)
admin.site.register(addtocarts2)
