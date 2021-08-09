from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Student

def homepage(request):
    return render(request, "my_lms/index.html")

def user_login(request):
    # if user is loggedin go to home page
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Username OR Password is incorrect.')
    return render(request, 'my_lms/login.html')

def user_logout(request):
    logout(request)
    return redirect('login_page')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            print(user)
            return redirect('login_page')
    context = {'form':form}
    return render(request, 'my_lms/register.html', context)

def create_student(request):
    student = Student()
    if request.method == "POST":
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        cnic = request.POST.get('cnic')
        course_enrolled = request.POST.get('course_enrolled')
        cgpa = request.POST.get('cgpa')
        student.name = name
        student.phone_no = phone_no
        student.cnic = cnic
        student.course_enrolled = course_enrolled
        student.cgpa = cgpa
        student.save()
        return redirect("students_record")
    return render(request, 'my_lms/student_form.html', {'student': student})


def read_students(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, 'my_lms/all_students.html', context)

def update_student(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        cnic = request.POST.get('cnic')
        course_enrolled = request.POST.get('course_enrolled')
        cgpa = request.POST.get('cgpa')
        student.name = name
        student.phone_no = phone_no
        student.cnic = cnic
        student.course_enrolled = course_enrolled
        student.cgpa = cgpa
        student.save()
        return redirect("students_record")
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'my_lms/student_form.html', {'student': student})

def delete_student(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        student.delete()
        return redirect("students_record")
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'my_lms/confirm_delete.html', {'student': student})

def search_student(request):
    if request.method=='POST':
        searched = request.form['searched']
    return render(request, 'my_lms/searchbox.html')

def search_result(request, s):
    students = Student.objects.all()
    return render(request, 'my_lms/Search.html', {'searched':s, 'students':students})