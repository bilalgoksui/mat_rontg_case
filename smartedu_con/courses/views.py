from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render ,redirect
from .models import Category, Course, Tag
from .forms import CourseForm
from django.contrib.auth.decorators import user_passes_test



def course_list(request,category_slug =None,tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    current_user = request.user
    if category_slug !=None:
        category_page = get_object_or_404(Category,slug=category_slug)
        courses = Course.objects.filter(avaliable=True,category=category_page)
    
    elif tag_slug !=None:
        tag_page = get_object_or_404(Tag,slug=tag_slug)
        courses = Course.objects.filter(avaliable=True,tags=tag_page)


    else:
          
        if current_user.is_authenticated:
            enrolled_courses = current_user.courses_joined.all()
            courses = Course.objects.all().order_by('-date')

            for course in enrolled_courses:
                courses = courses.exclude(id=course.id)

        else:
            courses = Course.objects.all()
    context = {
        'courses':courses,
        'categories':categories,
        'tags': tags
    }
    
    return render(request,'courses.html', context)


def course_detail(request, category_slug, course_id):
    current_user = request.user
    
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    courses = Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()

        if hasattr(current_user, 'teacher'):  
            user_role = current_user.teacher.role
        else:
            user_role = None
    else:
        enrolled_courses = courses
        user_role = None
        
    context = {
        'course': course,
        'enrolled_courses': enrolled_courses,
        'categories': categories,
        'tags': tags,
        'teacher_role': user_role  
    }
    print("*********",user_role)
    return render(request, 'course.html', context)



def search(request):
    courses = Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'courses':courses,
        'categories':categories,
        'tags': tags
    }
    return render(request,'courses.html', context)
    
    
    
    
def search(request):
    courses = Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'courses':courses,
        'categories':categories,
        'tags': tags
    }
    return render(request,'courses.html', context)
    



def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin)
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')  
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})


# @user_passes_test(lambda user: user.is_authenticated and user.teacher.role == 'Admin')
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if not request.user.is_staff and course.teacher != request.user.teacher:
        return HttpResponseForbidden("You are not authorized to delete this course.")
    
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    else:
        return redirect('course_detail', course_id=course_id)


# def course_list(request):
    
#     courses = Course.objects.all().order_by('date')
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         'courses':courses,
#         'categories':categories,
#         'tags': tags
#     }
#     return render(request,'courses.html', context)



# def category_list(request,category_slug):
#     courses = Course.objects.all().filter(category__slug=category_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         'courses':courses,
#         'categories':categories,
#         'tags':tags
#     }
 
#     return render(request,'courses.html', context)


# def tag_list(request,tag_slug):
#     courses = Course.objects.all().filter(tags__slug=tag_slug)
#     tags = Tag.objects.all()
#     context = {
#         'courses':courses,
#         'tags':tags
#     }
 
#     return render(request,'courses.html', context)