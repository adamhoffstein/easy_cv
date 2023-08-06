from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "company-autocomplete",
        views.CompanyAutocomplete.as_view(
            create_field="name", validate_create=True
        ),
        name="company-autocomplete",
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
        name="job_description_delete",
    ),
    path(
        "tags",
        views.TagListView.as_view(),
        name="tag_list",
    ),
    path(
        "tags/add/",
        views.TagCreateView.as_view(),
        name="tag_add",
    ),
    path(
        "tags/edit/<int:pk>/",
        views.TagUpdateView.as_view(),
        name="tag_edit",
    ),
    path(
        "tags/details/<int:pk>/",
        views.TagDetailView.as_view(),
        name="tag_details",
    ),
    path(
        "tags/delete/<int:pk>/",
        views.TagDeleteView.as_view(),
        name="tag_delete",
    ),
    path(
        "tags/bulk_import/",
        views.TagBulkImportView.as_view(),
        name="tag_bulk_import",
    ),
    path(
        "companies",
        views.CompanyListView.as_view(),
        name="company_list",
    ),
    path(
        "companies/add/",
        views.CompanyCreateView.as_view(),
        name="company_add",
    ),
    path(
        "companies/edit/<int:pk>/",
        views.CompanyUpdateView.as_view(),
        name="company_edit",
    ),
    path(
        "companies/details/<int:pk>/",
        views.CompanyDetailView.as_view(),
        name="company_details",
    ),
    path(
        "companies/delete/<int:pk>/",
        views.CompanyDeleteView.as_view(),
        name="company_delete",
    ),
    path(
        "resume_jobs",
        views.ResumeJobListView.as_view(),
        name="resume_job_list",
    ),
    path(
        "resume_jobs/add/",
        views.ResumeJobCreateView.as_view(),
        name="resume_job_add",
    ),
    path(
        "resume_jobs/edit/<int:pk>/",
        views.ResumeJobUpdateView.as_view(),
        name="resume_job_edit",
    ),
    path(
        "resume_jobs/details/<int:pk>/",
        views.ResumeJobDetailView.as_view(),
        name="resume_job_details",
    ),
    path(
        "resume_jobs/delete/<int:pk>/",
        views.ResumeJobDeleteView.as_view(),
        name="resume_job_delete",
    ),
    path(
        "resumes",
        views.ResumeListView.as_view(),
        name="resume_list",
    ),
    path(
        "resumes/add/",
        views.ResumeCreateView.as_view(),
        name="resume_add",
    ),
    path(
        "resumes/edit/<int:pk>/",
        views.ResumeUpdateView.as_view(),
        name="resume_edit",
    ),
    path(
        "resumes/details/<int:pk>/",
        views.ResumeDetailView.as_view(),
        name="resume_details",
    ),
    path(
        "resumes/delete/<int:pk>/",
        views.ResumeDeleteView.as_view(),
        name="resume_delete",
    ),
    path(
        "resume_education",
        views.ResumeEducationListView.as_view(),
        name="resume_education_list",
    ),
    path(
        "resume_education/add/",
        views.ResumeEducationCreateView.as_view(),
        name="resume_education_add",
    ),
    path(
        "resume_education/edit/<int:pk>/",
        views.ResumeEducationUpdateView.as_view(),
        name="resume_education_edit",
    ),
    path(
        "resume_education/details/<int:pk>/",
        views.ResumeEducationDetailView.as_view(),
        name="resume_education_details",
    ),
    path(
        "education/delete/<int:pk>/",
        views.ResumeEducationDeleteView.as_view(),
        name="resume_education_delete",
    ),
]
