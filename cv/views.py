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
    TagBulkImportForm,
    TagCategoryForm,
)
from .models import (
    JobDescription,
    Tag,
    TagCategory,
    Company,
    ResumeJob,
    Resume,
    ResumeEducation,
)


class CreatedByView(generic.CreateView):
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.last_edited_by = self.request.user
        return super(CreatedByView, self).form_valid(form)


class EditedByView(generic.UpdateView):
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.last_edited_by = self.request.user
        return super(EditedByView, self).form_valid(form)


def index(request):
    return render(request, "cv/index.html")


class CompanyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return (
            Company.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-name")
        )


class TagCategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return (
            TagCategory.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-name")
        )


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return (
            Tag.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-name")
        )


class TagBulkImportView(generic.edit.FormView):
    template_name = "cv/tag_bulk_import_form.html"
    form_class = TagBulkImportForm
    success_url = "/tags"

    def form_valid(self, form):
        for tag in [
            t.strip().title() for t in form.cleaned_data["tags"].split(",")
        ]:
            if not Tag.objects.filter(name=tag).first():
                Tag.objects.create(
                    name=tag,
                    keywords=tag,
                    category=form.cleaned_data["category"],
                    show_in_cv=form.cleaned_data["show_in_cv"],
                    created_by=self.request.user,
                    last_edited_by=self.request.user,
                )
        return super().form_valid(form)


class TagCreateView(CreatedByView):
    model = Tag
    form_class = TagForm


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    paginate_by = 10

    def get_queryset(self) -> list[Tag]:
        return (
            Tag.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-created_at")
        )


class TagUpdateView(EditedByView):
    model = Tag
    form_class = TagForm

    def get_queryset(self):
        return Tag.objects.filter(created_by=self.request.user).all()


class TagDetailView(generic.DetailView):
    model = Tag
    context_object_name = "tag"

    def get_queryset(self):
        return Tag.objects.filter(created_by=self.request.user).all()


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tag_list")


class JobDescriptionCreateView(CreatedByView):
    model = JobDescription
    form_class = JobDescriptionForm


class JobDescriptionListView(generic.ListView):
    model = JobDescription
    context_object_name = "job_description_list"
    paginate_by = 10

    def get_queryset(self) -> list[JobDescription]:
        return (
            JobDescription.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-created_at")
        )


class JobDescriptionUpdateView(EditedByView):
    model = JobDescription
    form_class = JobDescriptionForm

    def get_queryset(self):
        return JobDescription.objects.filter(
            created_by=self.request.user
        ).all()


class JobDescriptionDetailView(generic.DetailView):
    model = JobDescription
    context_object_name = "job_description"

    def get_queryset(self):
        return JobDescription.objects.filter(
            created_by=self.request.user
        ).all()


class JobDescriptionDeleteView(generic.DeleteView):
    model = JobDescription
    success_url = reverse_lazy("job_description_list")


class CompanyCreateView(CreatedByView):
    model = Company
    fields = ["name"]


class CompanyListView(generic.ListView):
    model = Company
    context_object_name = "company_list"
    paginate_by = 10

    def get_queryset(self) -> list[Tag]:
        return (
            Company.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-created_at")
        )


class CompanyUpdateView(EditedByView):
    model = Company
    form_class = CompanyForm

    def get_queryset(self):
        return Tag.objects.filter(created_by=self.request.user).all()


class CompanyDetailView(generic.DetailView):
    model = Company
    context_object_name = "company"

    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user).all()


class CompanyDeleteView(generic.DeleteView):
    model = Company
    success_url = reverse_lazy("company_list")


class ResumeJobCreateView(CreatedByView):
    model = ResumeJob
    form_class = ResumeJobForm


class ResumeJobListView(generic.ListView):
    model = ResumeJob
    context_object_name = "resumejob_list"
    paginate_by = 10

    def get_queryset(self) -> list[ResumeJob]:
        return (
            ResumeJob.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-created_at")
        )


class ResumeJobUpdateView(EditedByView):
    model = ResumeJob
    form_class = ResumeJobForm

    def get_queryset(self):
        return ResumeJob.objects.filter(created_by=self.request.user).all()


class ResumeJobDetailView(generic.DetailView):
    model = ResumeJob
    context_object_name = "resumejob"

    def get_queryset(self):
        return ResumeJob.objects.filter(created_by=self.request.user).all()


class ResumeJobDeleteView(generic.DeleteView):
    model = ResumeJob
    success_url = reverse_lazy("resume_job_list")


class ResumeCreateView(CreatedByView):
    model = Resume
    form_class = ResumeForm


class ResumeListView(generic.ListView):
    model = Resume
    context_object_name = "resume_list"
    paginate_by = 10

    def get_queryset(self) -> list[Resume]:
        return (
            Resume.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-created_at")
        )


class ResumeUpdateView(EditedByView):
    model = Resume
    form_class = ResumeForm

    def get_queryset(self):
        return Resume.objects.filter(created_by=self.request.user).all()


class ResumeDetailView(generic.DetailView):
    model = Resume
    context_object_name = "resume"

    def get_queryset(self):
        return Resume.objects.filter(created_by=self.request.user).all()


class ResumeDeleteView(generic.DeleteView):
    model = Resume
    success_url = reverse_lazy("resume_list")


class ResumeEducationCreateView(CreatedByView):
    model = ResumeEducation
    form_class = ResumeEducationForm


class ResumeEducationListView(generic.ListView):
    model = ResumeEducation
    context_object_name = "resume_education_list"
    paginate_by = 10

    def get_queryset(self) -> list[ResumeEducation]:
        return (
            ResumeEducation.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-created_at")
        )


class ResumeEducationUpdateView(EditedByView):
    model = ResumeEducation
    form_class = ResumeEducationForm

    def get_queryset(self):
        return ResumeEducation.objects.filter(
            created_by=self.request.user
        ).all()


class ResumeEducationDetailView(generic.DetailView):
    model = ResumeEducation
    context_object_name = "resume_education"

    def get_queryset(self):
        return ResumeEducation.objects.filter(
            created_by=self.request.user
        ).all()


class ResumeEducationDeleteView(generic.DeleteView):
    model = ResumeEducation
    success_url = reverse_lazy("resume_education_list")


class TagCategoryCreateView(generic.edit.FormView):
    template_name = "cv/tagcategory_form.html"
    form_class = TagCategoryForm
    success_url = "/tag_categories"

    def form_valid(self, form):
        tag_category = TagCategory.objects.create(
            name=form.cleaned_data["name"],
            created_by=self.request.user,
            last_edited_by=self.request.user,
        )
        tag_category.tags.set(form.cleaned_data["tags"].all())
        return super().form_valid(form)


class TagCategoryListView(generic.ListView):
    model = Tag
    context_object_name = "tag_category_list"
    paginate_by = 10

    def get_queryset(self) -> list[Tag]:
        return (
            TagCategory.objects.filter(created_by=self.request.user)
            .all()
            .order_by("-created_at")
        )


class TagCategoryUpdateView(generic.edit.FormView):
    template_name = "cv/tagcategory_form.html"
    form_class = TagCategoryForm
    success_url = "/tag_categories"

    def get_initial(self):
        initial = super().get_initial()
        tag_category = TagCategory.objects.get(
            id=self.kwargs["pk"], created_by=self.request.user
        )
        initial["name"] = tag_category.name
        initial["tags"] = tag_category.tags.all()
        return initial

    def form_valid(self, form):
        tag_category = TagCategory.objects.get(
            id=self.kwargs["pk"], created_by=self.request.user
        )
        tag_category.name = form.cleaned_data["name"]
        tag_category.tags.set(form.cleaned_data["tags"].all())
        tag_category.last_edited_by = self.request.user
        tag_category.save()
        return super().form_valid(form)


class TagCategoryDetailView(generic.DetailView):
    model = TagCategory
    context_object_name = "tag_category"

    def get_queryset(self):
        return TagCategory.objects.filter(created_by=self.request.user).all()


class TagCategoryDeleteView(generic.DeleteView):
    model = TagCategory
    context_object_name = "tag_category"
    success_url = reverse_lazy("tag_category_list")
