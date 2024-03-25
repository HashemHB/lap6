from django.urls import path
from .views import students, add_student, courses, add_course, details

urlpatterns = [
    path('students/', students, name='students'),
    path('add_student/', add_student, name='add_student'),
    path('courses/', courses, name='courses'),
    path('add_course/', add_course, name='add_course'),
    path('details/<int:student_id>/', details, name='details'),
]
