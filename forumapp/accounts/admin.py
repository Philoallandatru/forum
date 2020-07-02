from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
admin.site.site_header = "社交论坛系统管理员界面"