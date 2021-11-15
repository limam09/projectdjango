from django.contrib import admin

from bookstore.views import search

# Register your models here.

from .models import *

class AdminArticle(admin.ModelAdmin):
    list_display=('title','category','created_at','updated_at')
    search_fields =('title',)
    list_filter = ('created_at',)


class AdminCommand(admin.ModelAdmin):
    list_display = ('nom','email','address','ville','pays','date_commande')
    search_fields =('nom',)
    list_editable =('email','address',)

admin.site.site_header = "Limam_Bibliotheque"
admin.site.site_title = "Manageur"
admin.site.index_title = "Manageur"
admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Article,AdminArticle)
#admin.site.register(Article,AdminArticle)
admin.site.register(Commande,AdminCommand)
# admin.site.register(Category)
# admin.site.register(Image)
# admin.site.register(Notification)
