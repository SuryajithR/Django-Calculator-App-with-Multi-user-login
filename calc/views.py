from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from calc.models import teacher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *


# Create your views here.

def teacher_home(request):
    stu = teacher.objects.all().order_by('rno')
    paginator = Paginator(stu, 100)
    page = request.GET.get('page')
    try:
        studs = paginator.page(page)
    except PageNotAnInteger:
        studs = paginator.page(1)
    except EmptyPage:
        studs = paginator.page(paginator.num_pages)

    context = {'stu':stu, 'studs':studs}
    return render(request, 'teacherhome.html', context)


def add_student(request):
    stu= studentform()
    if request.method=='POST':
        stu=studentform(request.POST, request.FILES)
        if stu.is_valid():
            stu.save()
        return redirect('teacher')
    return render(request, "add-student.html", {'stu':stu})    


def student_home(request):
    details = teacher.objects.filter(name=request.user)
    # total=teacher.objects.aggregate(Sum('subject1'))

    return render(request, 'studenthome.html', {'details':details})
