from django.urls import path
from .views import *

urlpatterns=[
    path('register',register_view.as_view(),name="register"), # url for registering a user
    path('login',login_view.as_view(),name="login"),          # url for logging in a user
    path('logout',logout_view.as_view(),name="logout"),       # url for logging out a user
]