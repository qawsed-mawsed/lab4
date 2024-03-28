from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avia.urls')),

    # Добавь другие URL-маршруты, если необходимо
]
