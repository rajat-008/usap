from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

from .models import *
# Create your views here.


def index(request):
    return render(request,"login.html")

def login(request):
    if request.user.is_authenticated:
        return redirect(index)
    username=request.POST.get('username')
    password=request.POST.get('password')
    type=request.POST.get('type')
    if(type=='Student'):
        stud=Student.objects.get(student_name=username)
        if not stud:
            return HttpResponse("youre not a student")
    if(type=='Degree_provider'):
        stud=degree_provider.objects.get(degree_provider_name=username)
        if not stud:
            return HttpResponse("youre not a degree provider")
    if(type=='Course_provider'):
        stud=course_provider.objects.get(course_provider_name=username)
        if not stud:
            return HttpResponse("youre not a course provider")
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request,user)
        request.session['user_name']=username
        request.session['type'] = type
        request.session['id']=stud
        return redirect(index)
    else:
        return HttpResponse("Your username and password didn't match.")
