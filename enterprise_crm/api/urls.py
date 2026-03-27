
from django.urls import path
from .import views
urlpatterns = [
    path('cus/',views.CustomerApiView),
    path('api/', views.CustomerHomeApiView),
    path('apiview/',views.CustomerListApiView),
    path('apiview/<int:id>/',views.CustomerDetailApiView),
]