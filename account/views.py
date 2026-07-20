from django.shortcuts import render, redirect
from .forms import UserCreateForm
from .models import UserRole
from django.contrib import messages

# Create your views here.
def create_account(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.role = UserRole.objects.get(id=1)
            user.set_password(password)
            user.save()
            messages.success(request, "You are successfully registered.")
            return redirect('register_school')
    else:
        form = UserCreateForm()

    return render(request, 'account/create_account.html', {'form':form})

def super_admin_dashboard(request):
    return render(request, 'account/super_admin_dashboard.html')

def admin_dashboard(request):
    return render(request, 'account/admin_dashboard.html')

def principal_dashboard(request):
    return render(request, 'account/principal_dashboard.html')

def accountant_dashboard(request):
    return render(request, 'account/accountant_dashboard.html')

def teacher_dashboard(request):
    return render(request, 'account/teacher_dashboard.html')

def class_teacher_dashboard(request):
    return render(request, 'account/class_teacher_dashboard.html')

def transporter_dashboard(request):
    return render(request, 'account/transporter_dashboard.html')

def cundoctor_dashboard(request):
    return render(request, 'account/cundoctor_dashboard.html')

def parent_dashboard(request):
    return render(request, 'account/parent_dashboard.html')