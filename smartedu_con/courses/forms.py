from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['teacher', 'students', 'grade', 'name', 'category', 'tags', 'description', 'image', 'pdf', 'avaliable']
        labels = {
            'teacher': 'Teacher:',
            'students': 'Students:',
            'grade': 'Grade:',
            'name': 'Name:',
            'category': 'Category:',
            'tags': 'Tags:',
            'description': 'Description:',
            'image': 'Image:',
            'pdf': 'PDF:',
            'avaliable': 'Available:'
        }
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
            'pdf': forms.FileInput(attrs={'accept': 'application/pdf'}),
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['pdf'].required = False
        self.fields['students'].required = False
