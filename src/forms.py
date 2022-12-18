from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput



class employee_form(forms.Form):
    username = forms.CharField(label='Employee Username (enter username without space)', max_length=50)
    postion = forms.CharField(label='Employee Position', max_length=100)
    phone = forms.CharField(label='Employee Phone', max_length=20)
    salary = forms.IntegerField()
    
class update_employee_form(forms.ModelForm):
    class Meta:
        model   = employee
        exclude = ('role_admin_id' , 'user' , 'otp')

class profileUpdate(forms.ModelForm):
    class Meta:
        model   = employee_profile
        fields = (
            "name",
            "email",
            "about",
            "image"
        )
        




# class attendance_form(forms.ModelForm):
#     date = forms.DateField(label="Select Date",required=True, widget=NumberInput(attrs={'type':'date'}))   
#     class Meta:
#         model = attendance
#         exclude = ('employee_id',)


# class salary_form(forms.ModelForm):
#     date = forms.DateField(label="Select Date",required=True, widget=NumberInput(attrs={'type':'date'}))   
#     class Meta:
#         model = salary
#         exclude = ('employee_id',)


# class project_tracking_form(forms.ModelForm):
#     class Meta:
#         model = project_tracking
#         exclude = ('employee_id',)
