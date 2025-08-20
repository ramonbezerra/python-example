from django.urls import include, path
# from .views import courses_list, course_detail, course_create, course_update, course_delete
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

appname = 'school'

urls = [
    # path('courses/', courses_list, name='courses_list'),
    path('courses/', CourseListView.as_view(), name='courses_list'),

    # path('courses/<int:pk>', course_detail, name='course_detail'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course_detail'),

    # path('courses/create/', course_create, name='course_create'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),

    # path('courses/<int:pk>/update/', course_update, name='course_update'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),

    # path('courses/<int:pk>/delete/', course_delete, name='course_delete'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
]

school_patterns = (urls, appname)

urlpatterns = [
    path('', include(school_patterns))
]