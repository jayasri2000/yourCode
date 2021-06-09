"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views import css_course, get_started, html_course, index, js_course
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('get-started', get_started, name='get-started'),
    path('courses/html', html_course, name='html-course'),
    path('courses/css', css_course, name='css-course'),
    path('courses/javascript', js_course, name='js-course'),
]
