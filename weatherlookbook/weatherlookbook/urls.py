from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crawlingapp/', include('crawlingapp.urls')),
    path('accountapp/', include('accountapp.urls')),
]
