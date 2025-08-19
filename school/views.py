from django.shortcuts import render, redirect, get_object_or_404
from school.forms import CourseForm
from school.models import Course

# Create your views here.
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'school/list.html', {'courses': courses})

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'school/detail.html', {'course': course})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if not form.is_valid():
            return render(request, 'school/create.html', {'form': form})
        else:
            course = Course.objects.create(**form.cleaned_data)
            course.save()
            return redirect('school:course_detail', pk=course.pk)
    return render(request, 'school/create.html', {'form': CourseForm()})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if not form.is_valid():
            return render(request, 'school/update.html', {'form': form, 'course': course })
        else:
            form.save()
            return redirect('school:courses_list')
    else:
        return render(request, 'school/update.html', {'form': form, 'course': course })