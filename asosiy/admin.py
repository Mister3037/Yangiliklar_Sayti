from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']



@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ["sarlavha", "sl_url", "publish_time", "status", "category"]
    prepopulated_fields = {"sl_url": ("sarlavha",)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "message"]


