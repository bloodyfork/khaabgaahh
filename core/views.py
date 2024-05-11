from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from خوابگاه.models import User
# Create your views here.


class LoginStudent(LoginView):
    template_name = "home/login.html"

    def post(self, request, *args, **kwargs):

        username = request.POST.get('student_number')
        password = request.POST.get('password')
        user = authenticate(request, phone=username, password=password)
        if user is not None:
            User.objects.get_or_create(user=user)
            login(request, user)
            return redirect(to='home')

        else:
            messages.info(request, "incorrect Password or Phone number")
            return render(request, 'home/login.html')