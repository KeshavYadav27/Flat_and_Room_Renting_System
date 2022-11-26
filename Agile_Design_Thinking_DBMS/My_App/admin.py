from django.contrib import admin
from .models import User,customer,owner,customer_phone,owner_phone,booking,owner_property,property_images

# Register your models here.
admin.site.register(User)
admin.site.register(customer)
admin.site.register(customer_phone)
admin.site.register(owner)
admin.site.register(owner_phone)
admin.site.register(owner_property)
admin.site.register(property_images)
admin.site.register(booking)