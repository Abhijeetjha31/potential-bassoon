from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.depart,name='depart-data'),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('detail/<int:pk>/',views.detail,name="detail"),
    path('add',views.add,name="add"),
    path('open_notebook/<int:id>/', views.open_notebook, name='open_notebook'),
    # path('notebook/<int:id>/',views.notebook_view, name='notebook'),
    path('open_notepad/<int:id>/', views.open_notepad, name='open_notepad'),
]
