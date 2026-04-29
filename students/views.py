from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ExamForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def exam_form(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        course = request.POST.get('course')
        year = request.POST.get('year')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        
        exam_form = ExamForm(
            full_name=full_name,
            course=course,
            year=year,
            address=address,
            phone_number=phone_number
        )
        exam_form.save()
        return render(request, 'success.html', {'form': exam_form})
    
    return render(request, 'exam_form.html')