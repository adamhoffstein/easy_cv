from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "job_descriptions",
        views.JobDescriptionListView.as_view(),
        name="job_description_list",
    ),
    path(
        "job_descriptions/add/",
        views.JobDescriptionCreateView.as_view(),
        name="job_description_add",
    ),
    path(
        "job_descriptions/edit/<int:pk>/",
        views.JobDescriptionUpdateView.as_view(),
        name="job_description_edit",
    ),
    path(
        "job_descriptions/details/<int:pk>/",
        views.JobDescriptionDetailView.as_view(),
        name="job_description_details",
    ),
    path(
        "job_descriptions/delete/<int:pk>/",
        views.JobDescriptionDeleteView.as_view(),
        name="delete",
    ),
]
