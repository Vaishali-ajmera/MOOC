from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        RedirectView.as_view(pattern_name="courses:course_list", permanent=False),
        name="home",
    ),
    path("accounts/", include("accounts.urls")),
    path("courses/", include("courses.urls")),
    path("enrollments/", include("enrollments.urls")),
]
