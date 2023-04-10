from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('get/', include('appGET_crawler.urls')),
    path('admin/', admin.site.urls),
]
