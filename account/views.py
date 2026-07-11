from django.shortcuts import render

# Create your views here.
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