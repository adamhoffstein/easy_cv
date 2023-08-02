from django.urls import reverse_lazy
from django.views import generic

from .forms import JobDescriptionForm
from .models import JobDescription


class JobDescriptionCreateView(generic.CreateView):
    model = JobDescription
    fields = ["title", "raw_text", "company"]


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
    success_url = reverse_lazy("cv:list")
