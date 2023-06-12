from django.urls import path
from . views import *

urlpatterns = [
    path('',add_show,name="add_show"),
    path('delete/<int:id>/',delete_data,name="delete_data"),
    path('update/<int:id>/',update_data, name="update_data"),
]
