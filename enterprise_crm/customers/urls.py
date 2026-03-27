
from django.urls import path
from .import views
from django.contrib import admin
urlpatterns = [
    path('home/',views.CustomerView)
]

admin.site.site_header = 'Customer Relationship Management'
admin.site.site_title = 'CRM Project'
admin.site.index_title = 'Customer Relationship Management(CRM)'
