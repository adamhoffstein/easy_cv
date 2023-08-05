from dal import autocomplete
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    JobDescriptionForm,
    TagForm,
    CompanyForm,
    ResumeJobForm,
    ResumeForm,
    ResumeEducationForm,
)
from .models import (
    JobDescription,
    Tag,
    Company,
    ResumeJob,
    Resume,
    ResumeEducation,
)


def index(request):
    return render(request, "cv/index.html")


class CompanyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return Company.objects.all().order_by("-name")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name", "keywords"]


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    paginate_by = 10

    def get_queryset(self) -> list[Tag]:
        return Tag.objects.all().order_by("-created_at")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm

    def get_queryset(self):
        return Tag.objects.all()


class TagDetailView(generic.DetailView):
    model = Tag
    context_object_name = "tag"

    def get_queryset(self):
        return Tag.objects.all()


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tag_list")


class JobDescriptionCreateView(generic.CreateView):
    model = JobDescription
    form_class = JobDescriptionForm


class JobDescriptionListView(generic.ListView):
    model = JobDescription
    context_object_name = "job_description_list"
    paginate_by = 10

    def get_queryset(self) -> list[JobDescription]:
        return JobDescription.objects.all().order_by("-created_at")


class JobDescriptionUpdateView(generic.UpdateView):
    model = JobDescription
    form_class = JobDescriptionForm

    def get_queryset(self):
        return JobDescription.objects.all()


class JobDescriptionDetailView(generic.DetailView):
    model = JobDescription
    context_object_name = "job_description"

    def get_queryset(self):
        return JobDescription.objects.all()


class JobDescriptionDeleteView(generic.DeleteView):
    model = JobDescription
    success_url = reverse_lazy("job_description_list")


class CompanyCreateView(generic.CreateView):
    model = Company
    fields = ["name"]


class CompanyListView(generic.ListView):
    model = Company
    context_object_name = "company_list"
    paginate_by = 10

    def get_queryset(self) -> list[Tag]:
        return Company.objects.all().order_by("-created_at")


class CompanyUpdateView(generic.UpdateView):
    model = Company
    form_class = CompanyForm

    def get_queryset(self):
        return Tag.objects.all()


class CompanyDetailView(generic.DetailView):
    model = Company
    context_object_name = "company"

    def get_queryset(self):
        return Company.objects.all()


class CompanyDeleteView(generic.DeleteView):
    model = Company
    success_url = reverse_lazy("company_list")


class ResumeJobCreateView(generic.CreateView):
    model = ResumeJob
    form_class = ResumeJobForm


class ResumeJobListView(generic.ListView):
    model = ResumeJob
    context_object_name = "resumejob_list"
    paginate_by = 10

    def get_queryset(self) -> list[ResumeJob]:
        return ResumeJob.objects.all().order_by("-created_at")


class ResumeJobUpdateView(generic.UpdateView):
    model = ResumeJob
    form_class = ResumeJobForm

    def get_queryset(self):
        return ResumeJob.objects.all()


class ResumeJobDetailView(generic.DetailView):
    model = ResumeJob
    context_object_name = "resumejob"

    def get_queryset(self):
        return ResumeJob.objects.all()


class ResumeJobDeleteView(generic.DeleteView):
    model = ResumeJob
    success_url = reverse_lazy("resume_job_list")


class ResumeCreateView(generic.CreateView):
    model = Resume
    form_class = ResumeForm


class ResumeListView(generic.ListView):
    model = Resume
    context_object_name = "resume_list"
    paginate_by = 10

    def get_queryset(self) -> list[Resume]:
        return Resume.objects.all().order_by("-created_at")


class ResumeUpdateView(generic.UpdateView):
    model = Resume
    form_class = ResumeForm

    def get_queryset(self):
        return Resume.objects.all()


class ResumeDetailView(generic.DetailView):
    model = Resume
    context_object_name = "resume"

    def get_queryset(self):
        return Resume.objects.all()


class ResumeDeleteView(generic.DeleteView):
    model = Resume
    success_url = reverse_lazy("resume_list")


class ResumeEducationCreateView(generic.CreateView):
    model = ResumeEducation
    form_class = ResumeEducationForm


class ResumeEducationListView(generic.ListView):
    model = ResumeEducation
    context_object_name = "resume_education_list"
    paginate_by = 10

    def get_queryset(self) -> list[ResumeEducation]:
        return ResumeEducation.objects.all().order_by("-created_at")


class ResumeEducationUpdateView(generic.UpdateView):
    model = ResumeEducation
    form_class = ResumeEducationForm

    def get_queryset(self):
        return ResumeEducation.objects.all()


class ResumeEducationDetailView(generic.DetailView):
    model = ResumeEducation
    context_object_name = "resume_education"

    def get_queryset(self):
        return ResumeEducation.objects.all()


class ResumeEducationDeleteView(generic.DeleteView):
    model = ResumeEducation
    success_url = reverse_lazy("resume_education_list")
