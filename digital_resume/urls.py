from django.contrib import admin
from django.urls import path, inlcude

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inlcude('resume_site.urls')), 
]
