import re

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete
from .models import (
    JobDescription,
    Tag,
    Company,
    ResumeJob,
    Resume,
    ResumeEducation,
    TagCategory,
)
from django.core.exceptions import ValidationError


class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ("title", "raw_text", "company")
        widgets = {
            "company": autocomplete.ModelSelect2(url="company-autocomplete")
        }
        help_texts = {
            "raw_text": "Paste the raw text of the job description here"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save JobDescription"))


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name", "keywords", "category", "show_in_cv")
        widgets = {
            "category": autocomplete.ModelSelect2(
                url="tag-category-autocomplete"
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Tag"))


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Company"))


class ResumeJobForm(forms.ModelForm):
    class Meta:
        model = ResumeJob
        fields = (
            "title",
            "company",
            "company_description",
            "job_duty_raw_text",
            "start_at",
            "end_at",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Job"))


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
            "title",
            "jobs",
            "education",
            "skills",
            "languages",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Resume"))


class ResumeEducationForm(forms.ModelForm):
    class Meta:
        model = ResumeEducation
        fields = (
            "school",
            "degree",
            "location",
            "start_at_year",
            "end_at_year",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Education"))


class TagBulkImportForm(forms.Form):
    tags = forms.CharField(
        help_text="Enter one or more tags seperated by commas"
    )
    category = forms.ModelChoiceField(
        queryset=TagCategory.objects.all(),
        widget=autocomplete.ModelSelect2(url="tag-category-autocomplete"),
        required=False,
    )
    show_in_cv = forms.BooleanField(required=False)

    def clean_tags(self):
        data = self.cleaned_data["tags"]
        if not re.match(r"^[0-9a-zA-Z\-\s]+(,[0-9a-zA-Z\-\s]+)*$", data):
            raise ValidationError("Tags must be separated by commas")
        return data


class TagCategoryForm(forms.Form):
    name = forms.CharField()
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url="tag-autocomplete"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Tag"))
