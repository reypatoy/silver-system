from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    # login auth
    path("login/", login_view, name="login_view"),
    # apps
    path("crm/", include("crm.urls", namespace="crm")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# <a href href = {% url 'crm:add_pet_view' %}></a>
