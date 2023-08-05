from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete
from .models import JobDescription, Tag, Company, ResumeJob


class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ("title", "raw_text", "company")
        widgets = {
            "company": autocomplete.ModelSelect2(url="company-autocomplete")
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save JobDescription"))


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name", "keywords")

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
