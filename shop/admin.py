from django.contrib import admin
from shop.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","stock","oferta"]


admin.site.register(Employee,EmployeeAdmin)
