from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import home.views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home.views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
