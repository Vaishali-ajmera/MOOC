from django.urls import path

from courses.views import CourseDetailView, CourseListView, lesson_detail

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
    path("<slug:slug>/lessons/<int:pk>/", lesson_detail, name="lesson_detail"),
]
