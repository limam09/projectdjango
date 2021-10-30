from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Category)
# admin.site.register(Image)
