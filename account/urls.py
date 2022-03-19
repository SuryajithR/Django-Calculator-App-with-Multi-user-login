from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('home/', views.home, name='home'),
    # path('teacher_home/', views.teacher_home, name='teacher_home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
]