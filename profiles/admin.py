from django.contrib import admin
from .models import AdminUser, StaffUser, ClientUser, CustomUser

admin.site.register(CustomUser)
admin.site.register(AdminUser)
admin.site.register(StaffUser)
admin.site.register(ClientUser)
