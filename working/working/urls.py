from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include("view_working_profile.urls")),
]


