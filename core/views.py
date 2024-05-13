from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib import messages
from خوابگاه.models import User, Room


# Create your views here.


class LoginStudent(LoginView):
    template_name = "home/login.html"

    def post(self, request, *args, **kwargs):

        student_number = request.POST.get('student_number')
        password = request.POST.get('password')
        print(student_number)
        print(password)
        user = authenticate(request, student_number=student_number, password=password)
        if user is not None:
            print('kobs')
            User.objects.get_or_create(student_number=student_number)
            login(request, user)
            return redirect(to='reserve')

        else:
            print('no kobs')
            messages.info(request, "!نام کاربری یا رمز عبور اشتباه است")
            return render(request, 'home/login.html')


def logout_user(request):
    logout(request)
    return redirect(to='student_login')


class ReservePanel(ListView):
    template_name = 'home/reserve.html'
    model = Room



