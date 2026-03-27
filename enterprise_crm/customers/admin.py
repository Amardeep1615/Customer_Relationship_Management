from django.contrib import admin
from customers.models import  Customer
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','create_at')
    list_filter = ('email','phone','create_at')
    # list_editable = ('email','phone','create_at')
    search_fields = ('name','email','phone','create_at')
    list_per_page = 10
