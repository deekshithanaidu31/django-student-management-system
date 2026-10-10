
from django.urls import path
from . import views

urlpatterns = [
    # Display and search students
    path('', views.student_list, name='student_list'),

    # Add student
    path('add/', views.add_student, name='add_student'),

    # Edit student
    path('edit/<int:id>/', views.edit_student, name='edit_student'),

    # Delete student
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]
