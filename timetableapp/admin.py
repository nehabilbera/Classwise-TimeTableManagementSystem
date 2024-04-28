from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = "TimeTable Generator Administration"
admin.site.site_title = "TimeTable Admin"
admin.site.index_title = "Admin Page"

class ClassCourseDisp(admin.ModelAdmin):
    search_fields = ('class_id','professor_id','course_id')
    list_display = ('class_id','professor_id','course_id')
    list_editable = ('professor_id','course_id')

class CourseDisp(admin.ModelAdmin):
    search_fields = ('user','course_id','course_name')
    list_display = ('course_id','course_name', "course_type", "credit_hours", "department")
    # list_editable = ('course_id','course_name')

class ProfessorDisp(admin.ModelAdmin):
    search_fields = ("user", "professor_id", "professor_name", "professor_email")
    list_display = ("professor_id", "professor_name", "professor_email")
    
class DepartmentDisp(admin.ModelAdmin):
    search_fields = ("user", "branch_name", "department_name", "semester", "students_length")
    list_display = ("branch_name", "department_name", "semester", "students_length")
    
class ClassDisp(admin.ModelAdmin):
    search_fields = ("class_id", "class_name")
    list_display =  ("class_id", "class_name", "class_strength", "no_sessions")

admin.site.unregister(Group)

admin.site.register(Course,CourseDisp)
admin.site.register(Professor, ProfessorDisp)
admin.site.register(Class, ClassDisp)
admin.site.register(ClassCourse,ClassCourseDisp)
admin.site.register(Activity)
admin.site.register(Department, DepartmentDisp)