from django.shortcuts import render , redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import login, authenticate ,logout as deauth
from django.contrib.auth.decorators import login_required
from .forms import *
import random 

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username , password=password)
        if user:
            login(request , user)
            return redirect('home')
        else:
            messages.error(request , 'Invalid username or password')
            return redirect('sign-in')
    return render(request,'signin.html')


def signin_emp(request):
    if request.method=='POST':
        get_phone=request.POST.get('phone')
        if employee.objects.filter(phone=get_phone , status="Active").exists():
            otp=str(random.randint(1000 , 9999))
            employee.objects.filter(phone=get_phone).update(otp=otp)
            return render(request , 'otp.html' , context={'otp':otp , 'phone':get_phone})
        else:
            messages.success(request , f"No employee using this  {get_phone} phone number")
            return redirect('signin-emp')
    return render(request,'signin-emp.html')    

def verify_otp(request):
    if request.method=='POST':
        get_phone=request.POST.get('phone')
        get_otp=request.POST.get('otp')
        if employee.objects.filter(phone=get_phone , otp=get_otp).exists():
            emp=employee.objects.filter(phone=get_phone , otp=get_otp).first()
            user=emp.user
            login(request , user)
            return redirect('profile')
            
        else:
            messages.success(request , f"Wrong OTP")
    otp=str(random.randint(1000 , 9999))
    employee.objects.filter(phone=get_phone).update(otp=otp)
    return render(request,'otp.html' , context={'otp':otp , 'phone':get_phone})  

@login_required(login_url='signin-emp')        
def profile(request):
    employees=employee.objects.get(user=request.user)
    get_profile=employee_profile.objects.get(employee_id=employees)
    all_employees = employee.objects.filter(role_admin_id=employees.role_admin_id)
    context = {
        'emp':True ,
        'employee':employees ,
        'profile':get_profile ,
        'all_employees':all_employees
    }
    return render(request , 'profile.html' , context )

@login_required(login_url='signin-emp') 
def profile_update(request):
    get_emp=employee.objects.get(user=request.user)
    emp=employee_profile.objects.get(employee_id=get_emp)
    
    if request.method=='POST':
        form=profileUpdate(request.POST , request.FILES , instance=emp)
        if form.is_valid():
            fr=form.save()
            messages.success(request , 'Your Profile updated successfully')
            return redirect('profile')


    form = profileUpdate(instance=emp)
    context={
        'form':form ,
        'profile':emp ,
        'emp':True
    }
    return render(request , 'profile-update.html' , context)

def logout(request):
    deauth(request)
    messages.success(request , 'Logged out successfully')
    return redirect('sign-in')


@login_required(login_url='sign-in')
def home(request):
    if request.user.is_superuser:
        AdminRole = role_admin.objects.filter(user=request.user).first()
        if AdminRole:
            employees=  employee.objects.filter(role_admin_id=AdminRole)
            shifts =    employee_shift.objects.filter(role_admin_id=AdminRole)
            context={
                "employees":employees ,
                "shifts":shifts ,
                
            }
            return render(request , 'home.html' , context)
        else:
            role_admin.objects.create(user=request.user)
            context={}
            return render(request , 'home.html' , context)        
        



@login_required(login_url='sign-in')
def add_employee(request):
    if request.user.is_superuser:
        get_roladmin = role_admin.objects.filter(user=request.user).first()
        if request.method=='POST':
            username    = request.POST.get('username')
            postion     = request.POST.get('postion')
            get_phone   = request.POST.get('phone')
            Gsalary     = request.POST.get('salary')

            if User.objects.filter(username=username).exists():
                messages.success(request , f"An Employee Already Exists With  {username} Username")
                return redirect('add-employee')
            if employee.objects.filter(phone=get_phone).exists():
                messages.success(request , f"An Employee Already using  {get_phone} phone number")
                return redirect('add-employee')

            get_user=User.objects.create(username=username)
            get_emp=employee.objects.create(
                role_admin_id   =  get_roladmin ,       
                user            =  get_user ,
                postion         =  postion ,
                phone           = get_phone ,
                status          =  "Active" ,
                salary          =  Gsalary
            )
            employee_profile.objects.create(
                employee_id = get_emp ,
                phone = get_phone
            )
            messages.success(request , "Employee Added successfully")
            return redirect('home')
        form=employee_form()        
        return render(request , 'add_employee.html',{'form':form})
    else:
        messages.success(request , "You are not an Admin")
        return redirect('home')

    


@login_required(login_url='sign-in')
def update_employee(request , pk):
    employee_obj=employee.objects.get(pk=pk)
    if request.method=='POST':
        form=update_employee_form(request.POST , request.FILES , instance=employee_obj)
        if form.is_valid():
            fr=form.save()
            messages.success(request , 'Employee deatils updated successfully')
            return redirect('home')
    form=update_employee_form(instance=employee_obj)        
    return render(request , 'add_employee.html',{'form':form})


@login_required(login_url='sign-in')
def shift_management(request):
    getAdmin = role_admin.objects.filter(user=request.user).first()
    employees=employee.objects.filter(role_admin_id=getAdmin)
    shifts=employee_shift.objects.filter(role_admin_id=getAdmin)

    context={
        'employees':employees,
        'shifts':shifts
    }
    return render(request , 'shift_management.html' , context)

