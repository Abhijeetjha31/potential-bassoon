from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.depart,name='depart-data'),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('detail/<int:pk>/',views.detail,name="detail"),
    path('add',views.add,name="add"),
]