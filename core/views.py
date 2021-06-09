from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "core/index.html")


def get_started(request):
    return render(request, 'core/getstarted.html')

def html_course(request):
    return render(request, 'core/courses/html_course.html')

def css_course(request):
    return render(request, 'core/courses/css_course.html')

def js_course(request):
    return render(request, 'core/courses/js_course.html')