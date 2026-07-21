from django.shortcuts import render, redirect
from .forms import SchoolForm
from django.contrib import messages
from .models import School

# Create your views here.
def register_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        print(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            extra_field = {}
            extra_field['mobile'] = request.POST.get('mobile', '')
            extra_field['email'] = request.POST.get('email', '')
            extra_field['mode'] = request.POST.get('mode', '')
            extra_field['affiliation'] = request.POST.get('affiliation', '')

            School.extra_field = extra_field

            save_form.save()
            messages.success(request, 'Form is successfully saved')
            return redirect('register_school')
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = SchoolForm()

    return render(request, 'school/register_school.html', {'form':form})