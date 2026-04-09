from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import AppointmentForm, ContactForm

def home_view(request):
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == 'appointment':
            form = AppointmentForm(request.POST)
        else:
            form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Success!")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    context = {
        'services': Service.objects.all(),
        'departments': Department.objects.all(),
        'doctors': Doctor.objects.all(),
        'home': Home.objects.last(),
        'about': About.objects.last(),
        'test': Testimonial.objects.all(),
        'faq': FAQ.objects.all(),
        'location': 5,
        'doctor_count': Doctor.objects.count(),

        'appointment_form': AppointmentForm(),
        'contact_form': ContactForm(),
    }
    return render(request, 'index.html', context)

