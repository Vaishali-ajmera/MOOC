from django.urls import path

from enrollments.views import MyCoursesView, enroll

app_name = "enrollments"

urlpatterns = [
    path("enroll/<int:course_id>/", enroll, name="enroll"),
    path("my-courses/", MyCoursesView.as_view(), name="my_courses"),
]
