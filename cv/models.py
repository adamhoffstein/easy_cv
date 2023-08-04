from abc import abstractmethod

from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    name = models.CharField(max_length=120, unique=True)
    keywords = models.CharField(
        max_length=500,
        validators=[
            RegexValidator(
                regex="^[0-9a-zA-Z\s]+(,[0-9a-zA-Z\s]+)*$",
                message="Keywords must be separated by commas",
                code="invalid_comma_separation",
            ),
        ],
    )
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if self.keywords:
            self.keywords = self.keywords.replace(" ", "").lower()
        super(Tag, self).save(*args, **kwargs)

    def get_keywords(self) -> list[str]:
        return self.keywords.split(",")

    def get_absolute_url(self):
        return reverse("tag_details", kwargs={"pk": self.pk})


class Company(BaseModel):
    name = models.CharField(max_length=120, unique=True, blank=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def get_absolute_url(self):
        return reverse("company_details", kwargs={"pk": self.pk})


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
    raw_text = models.TextField(max_length=5000, null=True)
    tags = models.ManyToManyField(Tag)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="job_descriptions"
    )
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.title

    def get_tags(self) -> None:
        jd_tags = []
        for tag in Tag.objects.all():
            for keyword in tag.get_keywords():
                if keyword in self.raw_text.lower() and tag not in jd_tags:
                    jd_tags.append(tag)
        return jd_tags

    def get_absolute_url(self):
        return reverse("job_description_details", kwargs={"pk": self.pk})


@receiver(post_save, sender=JobDescription)
def update_job_description_tags(sender, instance, created, **kwargs) -> None:
    if tags := instance.get_tags():
        instance.tags.set(tags)
