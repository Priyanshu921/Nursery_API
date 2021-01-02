from django.contrib import admin
from .models import user,Plant,Nursery,Order
# Register your models here.
admin.site.register(user)
admin.site.register(Plant)
admin.site.register(Nursery)
admin.site.register(Order)