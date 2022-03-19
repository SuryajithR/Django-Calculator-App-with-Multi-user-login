from django.conf.urls import url
from calc import views
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('register/', views.register, name='register'),
    path('teacher/', views.teacher_home, name='teacher'),
    path('student/', views.student_home, name='student'),
    path('add-student/', views.add_student, name='add'),
]
