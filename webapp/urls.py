from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("login",views.login_view),
    path("course_provider/dashboard",views.course_dashboard),
    path("course/register",views.course_register),
    path("course/details/<int:course_id>",views.course_details)
]
