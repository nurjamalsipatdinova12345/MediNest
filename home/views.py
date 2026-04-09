#
# from django.shortcuts import render
# from medinest.models import Service, Department, Doctor
# from .models import Home, About
#
# def home(request):
#     services = Service.objects.all()
#     departments = Department.objects.all()
#     doctors = Doctor.objects.all()
#     homes = Home.objects.last()
#     abouts = About.objects.last()
#     context = {
#         'services': services,
#         'departments': departments,
#         'doctors': doctors,
#         'home': homes,
#         'about': abouts,
#     }
#     return render(request, 'index.html', context)