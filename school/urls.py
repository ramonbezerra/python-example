from django.urls import include, path
from .views import courses_list, course_detail

appname = 'school'

urls = [
    path('', courses_list, name='courses_list'),
    path('<int:pk>', course_detail, name='course_detail'),
]

school_patterns = (urls, appname)

urlpatterns = [
    path('', include(school_patterns))
]