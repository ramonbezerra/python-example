from django.shortcuts import render

from school.models import Course

# Create your views here.
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'school/list.html', {'courses': courses})