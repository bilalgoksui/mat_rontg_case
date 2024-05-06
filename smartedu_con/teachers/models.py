from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

class User(AbstractUser):
    MASTER_ROLE = 'Master'
    TEACHER_ROLE = 'Teacher'
    STUDENT_ROLE = 'Student'
    
    ROLE_CHOICES = [
        (MASTER_ROLE, 'Master'),
        (TEACHER_ROLE, 'Teacher'),
        (STUDENT_ROLE, 'Student'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT_ROLE)



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="teachers/%Y/%m/%d/")
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.user.username

