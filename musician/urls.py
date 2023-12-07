from django.urls import path

from . import views 

urlpatterns=[
    path("",views.add_musician, name="add_musician"),
    path("edit_musician/<int:musician_id>", views.edit_musician, name="edit_musician"),
    
]