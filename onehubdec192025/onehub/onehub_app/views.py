from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        if models.User.objects.filter(email=email).exists():
            return HttpResponse(
                "<script>alert('Email already exists!'); window.location.href='/register/';</script>"
            )

        user = models.User(
            name=name,
            age=age,
            address=address,
            phone=phone,
            email=email,
            password=password,
            gender=gender,
            image=image,
        )
        user.save()
        return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = models.User.objects.get(email=email, password=password)
            request.session['email'] = email

            return redirect('userdashboard')
        except models.User.DoesNotExist:
            return HttpResponse(
                "<script>alert('Invalid email or password'); window.location.href='/login/';</script>"
            )

    return render(request, 'login.html')

def userdashboard(request):
    if 'email' not in request.session:
        return redirect('login')
    return render(request, 'userdashboard.html')


def profile(request):
    
    if 'email' in request.session:
        email = request.session.get('email')
        try:
            user = models.User.objects.get(email=email)
            return render(request,'profile.html',{'user':user})
        except models.User.DoesNotExist:
            return HttpResponse('user not found')
    return redirect('login')

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.gender = request.POST.get('gender')
        user.address = request.POST.get('address')

        if request.FILES.get('image'):
            user.image = request.FILES.get('image')

        user.save()
        return redirect('profile')

    return render(request, 'profile.html', {'user': user})


def logout(request):
    request.session.flush()
    return redirect('index')
