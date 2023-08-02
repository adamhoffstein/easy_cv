from abc import abstractmethod

from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from model_utils import fields


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = fields.AutoLastModifiedField()
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, null=True
    )
    last_edited_by = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(class)s_last_edited_by",
    )

    @property
    @abstractmethod
    def history(self) -> HistoricalRecords:
        pass

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=120, unique=True, blank=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name


class Company(BaseModel):
    name = models.CharField(max_length=120, unique=True, blank=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class ExperiencePoint(BaseModel):
    name = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)
    history = HistoricalRecords()


class Resume(BaseModel):
    title = models.CharField(max_length=120)
    experience_points = models.ManyToManyField(ExperiencePoint)
    history = HistoricalRecords()


class JobDescription(BaseModel):
    title = models.CharField(max_length=120)
    raw_text = models.CharField(max_length=5000, null=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="job_descriptions"
    )
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse("job_description_details", kwargs={"pk": self.pk})
