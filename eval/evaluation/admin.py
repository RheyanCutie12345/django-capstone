from django.contrib import admin
from .models import Users


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('LRN', 'Password', 'Name')
    search_fields = ('LRN', 'Name')


admin.site.register(Users, UserAdmin)
