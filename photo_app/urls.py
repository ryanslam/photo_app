from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('', include('photo_manager.urls')),
    path('admin/', admin.site.urls),
]
