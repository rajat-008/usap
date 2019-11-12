from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import login, logout, authenticate

from .models import *

def index(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return redirect(course_dashboard)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        type=request.POST.get('type')
        if(type=='student'):
            stud=Student.objects.filter(student_name=username)
            print(stud[0].id)
            if len(stud)==0:
                return render(request,"error.html",{"message":"you are not a student"})
        if(type=='degree_provider'):
            stud=degree_provider.objects.filter(deg_provider_name=username)
            if len(stud)==0:
                return render(request,"error.html",{"message":"you are not a degree provider"})
        if(type=='course_provider'):
            stud=course_provider.objects.filter(course_provider_name=username)
            if len(stud)==0:
                return render(request,"error.html",{"message":"you are not a course provider"})
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            request.session['user_name']=str(username)
            request.session['type'] = type
            request.session['id']=stud[0].id
            return redirect(index)
        else:
            return render(request,"error.html",{"message":"Your username and password didn't match."})
    return render(request,'login.html')


def course_dashboard(request):
    provider=course_provider.objects.filter(id=request.session['id'])[0]
    courses=course.objects.filter(course_provider=provider)
    return render(request,"course_dashboard.html",{"courses":courses})


def course_register(request):
    if request.method=="POST":
        print(request.session['id'])
        name=request.POST.get('course_name')
        desc=request.POST.get('desc')
        url=request.POST.get('url')
        duration=request.POST.get('duration')
        credits=request.POST.get('credit')
        provider=course_provider.objects.filter(id=request.session['id'])[0]
        cours=course(course_provider=provider,course_name=name,description=desc,url=url,duration=duration,credits=credits)
        cours.save()
        return redirect(course_dashboard)
    return render(request,"course_register.html")

def course_details(request,course_id):
    students=course_enroll.objects.filter(course__Co_id=course_id)
    return render(request,"course_details.html",{"students":students})
