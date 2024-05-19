from django.shortcuts import render


# Create your views here.

def student_panel(request):
    return render(request, 'student_panel/index3.html')
