from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.course_list,name='courses'),
    path('<slug:category_slug>/<int:course_id>',views.course_detail,name='course_detail'),
    path('categories/<slug:category_slug>',views.course_list,name='courses_by_category'),
    path('tags/<slug:tag_slug>',views.course_list,name='courses_by_tag'),
    path('search/',views.search,name='search'),
    path('create_course/',views.create_course,name='create_course'),
    path('course/<int:course_id>/delete/', views.delete_course, name='delete_course'),


]
