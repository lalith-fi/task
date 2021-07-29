from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    path('register',csrf_exempt(register_view.as_view()),name="register"), # url for registering a user
    path('login',csrf_exempt(login_view.as_view()),name="login"),          # url for logging in a user
    path('logout',logout_view.as_view(),name="logout"),       # url for logging out a user
]