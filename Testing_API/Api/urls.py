

# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import DepartmentsViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'departments', DepartmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

