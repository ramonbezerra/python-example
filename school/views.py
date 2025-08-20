from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from school.forms import CourseForm
from school.models import Course

# Create your views here.
# def courses_list(request):
#     courses = Course.objects.all()
#     return render(request, 'school/list.html', {'courses': courses})

class CourseListView(ListView):
    model = Course
    template_name = 'school/list.html'
    context_object_name = 'courses'

# def course_detail(request, pk):
#     course = Course.objects.get(pk=pk)
#     return render(request, 'school/detail.html', {'course': course})

class CourseDetailView(DetailView):
    model = Course
    template_name = 'school/detail.html'
    context_object_name = 'course'

# def course_create(request):
#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'school/create.html', {'form': form})
#         else:
#             course = Course.objects.create(**form.cleaned_data)
#             course.save()
#             return redirect('school:course_detail', pk=course.pk)
#     return render(request, 'school/create.html', {'form': CourseForm()})

class CourseCreateView(CreateView):
    model = Course
    template_name = 'school/create.html'
    form_class = CourseForm
    success_url = '/school/courses/'

# def course_update(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     form = CourseForm(instance=course)
#     if request.method == 'POST':
#         form = CourseForm(request.POST, instance=course)
#         if not form.is_valid():
#             return render(request, 'school/update.html', {'form': form, 'course': course })
#         else:
#             form.save()
#             return redirect('school:courses_list')
#     else:
#         return render(request, 'school/update.html', {'form': form, 'course': course })

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'school/update.html'
    form_class = CourseForm
    success_url = '/school/courses/'
    
# def course_delete(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     if request.method == 'POST':
#         course.delete()
#         return redirect('school:courses_list')
#     return render(request, 'school/delete.html', {'course': course})

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'school/delete.html'
    context_object_name = 'course'
    success_url = '/school/courses/'