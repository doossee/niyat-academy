from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Course

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'course_detail.html', {'course': course})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'layout/index.html', {'courses': courses})