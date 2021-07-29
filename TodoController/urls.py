from django.urls import path
from .views import *

urlpatterns=[
    path('getall',getall_view.as_view(),name="getall"),          # url for getting all the todoitems
    path('getone/<int:id>',getone_view.as_view(),name="getone"), # url for getting single todoitem
    path('create',create_view.as_view(),name="create"),          # url for creating a todoitem
    path('update/<int:id>',update_view.as_view(),name="update"), # url for updating a todoitem
    path('delete/<int:id>',delete_view.as_view(),name="delete")  # url for deleting a todoitem
]