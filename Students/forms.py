# Students/forms.py
from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'courses']  # Fields you want in the form

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']  # Fields you want in the form

class CourseRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        available_courses = kwargs.pop('available_courses')
        super(CourseRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['course'] = forms.ModelChoiceField(queryset=available_courses, empty_label="Select a course")