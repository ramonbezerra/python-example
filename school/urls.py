from django.urls import include, path
from .views import courses_list, course_detail, course_create, course_update, course_delete

appname = 'school'

urls = [
    path('courses/', courses_list, name='courses_list'),
    path('courses/<int:pk>', course_detail, name='course_detail'),
    path('courses/create/', course_create, name='course_create'),
    path('courses/<int:pk>/update/', course_update, name='course_update'),
    path('courses/<int:pk>/delete/', course_delete, name='course_delete'),
]

school_patterns = (urls, appname)

urlpatterns = [
    path('', include(school_patterns))
]