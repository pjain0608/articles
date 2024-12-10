from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('1',views.home, name = 'home'),
    path('2',views.about_me,name = 'about_me'),
    path('blog/<int:pk>/', views.blog, name='blog'),

]
