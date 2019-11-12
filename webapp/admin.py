from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Student)
admin.site.register(degree_provider)
admin.site.register(course_provider)
admin.site.register(degree)
admin.site.register(course)
admin.site.register(course_enroll)
admin.site.register(degree_enroll)
admin.site.register(degree_enroll_requirements)
