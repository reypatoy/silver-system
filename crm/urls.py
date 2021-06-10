from django.urls import path

from .views import admin_dashboard_view, add_pet_view

app_name = "crm"

urlpatterns = [
    path("dashboard/", admin_dashboard_view, name="admin_dashboard_view"),
    # path("add_pet/", add_pet_view, name="add_pet_view"),
    # /crm/add_pet
]


# 127.0.0.1:8000/api/v1/users CRUD
# 127.0.0.1:8000/api/v1/clients/pets

# heruko
# aws
