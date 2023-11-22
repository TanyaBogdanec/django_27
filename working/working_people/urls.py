from django.urls import path
from .views import view_working_profile


urlpatterns = [
    path('working_profile_view/', view_working_profile)
]