from django.urls import path
from .views import enroll, MyCoursesView

app_name = 'enrollments'

urlpatterns = [
    path('enroll/<int:course_id>/', enroll, name='enroll'),
    path('my-courses/', MyCoursesView.as_view(), name='my_courses'),
]
