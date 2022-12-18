from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(role_admin)
admin.site.register(employee)
admin.site.register(employee_profile)
admin.site.register(employee_shift)
admin.site.register(employee_salary)