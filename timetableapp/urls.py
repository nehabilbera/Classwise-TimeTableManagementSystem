
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # path('student_timetable/', views.student_timetable, name="student_timetable"),
    # path('student/', views.student_loginPage, name="student"),

    # path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.Logout, name="logout"),

    path('add-course/', views.CourseView, name='add-course'),
    path('course_view/', views.CourseTable, name='course_view'),
    path('update-course/<str:pk>/', views.updateCourseView, name='update-course'),
    path('delete-course/<str:pk>/', views.deleteCourse, name='delete-course'),

    path('add-professor/', views.ProfessorView, name='add-professor'),
    path('professor_view/', views.ProfessorTable, name='professor_view'),
    path('update-professor/<str:pk>/', views.updateProfessorView, name='update-professor'),
    path('delete-professor/<str:pk>/', views.deleteProfessor, name='delete-professor'),
    
    path('add-department/', views.DepartmentView, name='add-department'),
    path('deparment_view/', views.DepartmentTable, name='department_view'),
    path('update-department/<str:pk>/', views.updateDepartmentView, name='update-departmentview'),
    path('delete-department/<str:pk>/', views.deleteDepartment, name='delete-department'),
    
    path('add-class/', views.ClassView, name='add-class'),
    path('class-view/', views.ClassTable, name='class_view'),
    path('update-class/<str:pk>/', views.updateClassView, name='update-classview'),
    path('delete-class/<str:pk>/', views.deleteClass, name='delete-class'),

    path('add-classcourse/', views.ClassCourseView, name='add-classcourse'),
    path('classcourse/', views.ClassCourseTable, name='view-classcourse'),
    path('update-classcourse/<str:pk>/', views.updateClassCourse, name='update-classcourse'),
    path('delete-classcourse/<str:pk>/', views.deleteClassCourse, name='delete-classcourse'),



    path('generate-timetable/<str:id>/', views.GenerateTimeTable, name='generate-timetable'),
    path('timetable/<str:id>/', views.TimeTableView, name='timetable'),
    path('activity/<str:pk>/', views.AddActivity, name='add-activity'),
    

    
############    path('timetable/', views.TimeTable, name='timetable'), #############

]
