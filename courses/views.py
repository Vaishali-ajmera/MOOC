from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic import DetailView, ListView

from courses.models import Course, Lesson
from enrollments.models import Enrollment, LessonProgress


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_enrolled"] = False
        context["visited_lesson_ids"] = []

        if self.request.user.is_authenticated:
            context["is_enrolled"] = Enrollment.objects.filter(
                user=self.request.user, course=self.object
            ).exists()

            if context["is_enrolled"]:
                visited_lessons = LessonProgress.objects.filter(
                    user=self.request.user, lesson__course=self.object, visited=True
                ).values_list("lesson_id", flat=True)
                context["visited_lesson_ids"] = list(visited_lessons)

        return context


@login_required
def lesson_detail(request, slug, pk):
    course = get_object_or_404(Course, slug=slug)
    lesson = get_object_or_404(Lesson, pk=pk, course=course)

    is_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()

    if not is_enrolled:
        return redirect("courses:course_detail", slug=slug)

    LessonProgress.objects.update_or_create(
        user=request.user,
        lesson=lesson,
        defaults={"visited": True, "visited_at": timezone.now()},
    )

    lessons = course.lessons.all()
    current_index = list(lessons).index(lesson)
    previous_lesson = lessons[current_index - 1] if current_index > 0 else None
    next_lesson = (
        lessons[current_index + 1] if current_index < len(lessons) - 1 else None
    )

    context = {
        "course": course,
        "lesson": lesson,
        "previous_lesson": previous_lesson,
        "next_lesson": next_lesson,
    }

    return render(request, "courses/lesson_detail.html", context)
