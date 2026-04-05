from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_view),
    path('students/<int:pk>/', views.studentDetailView),
    path('employees/', views.Employee.as_view()),
    path('employees/<int:pk>/', views.EmployeeViewDetail.as_view()),
]