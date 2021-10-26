from django.urls import path

from apps.polls.views import dashboard, profile

app_name = "polls"
urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('profile/', profile, name="profile")
]
