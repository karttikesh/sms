from django.shortcuts import render

# Create your views here.
def register_school(request):
    return render(request, 'school/register_school.html')