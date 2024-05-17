from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib import messages
from خوابگاه.models import User, Room
from rest_framework.generics import UpdateAPIView
from خوابگاه.serializers import UserSerializer


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
            User.objects.get_or_create(student_number=student_number)
            login(request, user)
            return redirect(to='reserve')

        else:
            messages.info(request, "!نام کاربری یا رمز عبور اشتباه است")
            return render(request, 'home/login.html')


def logout_user(request):
    logout(request)
    return redirect(to='student_login')


class ReservePanel(ListView):
    template_name = 'home/reserve.html'
    model = Room


def change_password(request):
    return render(request, template_name='home/change_password.html')


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'student_number'

    def partial_update(self, request, *args, **kwargs):
        data = request.data

        student_number = data['student_number']
        new_pass1 = data['new_pass1']
        new_pass2 = data['new_pass2']
        old_pass = data['old_password']

        user = authenticate(request, student_number=student_number, password=old_pass)

        context = {}
        if user is not None:

            if new_pass1 == new_pass2:

                if new_pass1 == '' or new_pass2 == '':
                    message = '!هیچ فیلدی نمی تواند خالی باشد'
                    icon = 'error'

                    context['message'] = message
                    context['icon'] = icon
                    return JsonResponse(context, status=200)

                elif new_pass1 != old_pass:

                    the_user = User.objects.get(student_number=student_number)
                    the_user.password = new_pass1
                    the_user.save()

                    message = '!رمز ورود با موفقیت تغییر یافت'
                    icon = 'success'
                    context['message'] = message
                    context['icon'] = icon
                    return JsonResponse(context, status=200)

                else:
                    message = '!پسورد جدید و قدیمی نمی تواند یکی باشد'
                    icon = 'error'
                    context['message'] = message
                    context['icon'] = icon
                    return JsonResponse(context, status=200)

            else:
                message = '!رمز عبور جدید مطاقبت ندارد'
                icon = 'error'

                context['message'] = message
                context['icon'] = icon
                return JsonResponse(context, status=200)

        else:

            message = 'شماره ی دانشجویی یا رمز عبور اشتباه است'
            icon = 'error'
            context['message'] = message
            context['icon'] = icon
            return JsonResponse(context, status=200)
