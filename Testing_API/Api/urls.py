from django.urls import path
# from django.conf.urls import url
from Api import views
from .views import departmentApi,getbyid


urlpatterns = [
    path('department/', views.departmentApi, name='department'),
    path('department/<int:id>/',views.departmentApi),
    path('getbyId/<int:pk>/',views.getbyid),
    path('',views.getroutes),
]

# urlpatterns=[
#     path('getDepartment/',views.getDepartment),
# ]
