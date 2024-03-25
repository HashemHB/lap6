from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student,Course
from .forms import StudentForm, CourseForm 
from .forms import CourseRegistrationForm


def students(request):
    students_list=Student.objects.all()
    return render(request,'Students/students.html',{'students_list':students_list})

def courses(request):
    courses_list=Course.objects.all()
    return render(request,'Students/courses.html',{'courses_list':courses_list})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'Students/add_student.html', {'form': form})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')  # Use redirect here
    else:
        form = CourseForm()
    return render(request, 'Students/add_course.html', {'form': form})



def details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    registered_courses = student.courses.all()
    available_courses = Course.objects.exclude(pk__in=registered_courses)
    
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST, available_courses=available_courses)
        if form.is_valid():
            course = form.cleaned_data['course']
            student.courses.add(course)
            return redirect('details', student_id=student_id)
    else:
        form = CourseRegistrationForm(available_courses=available_courses)
    
    return render(request, 'Students/details.html', {'student': student, 'form': form})
# Create your views here.
