import re
from abc import abstractmethod

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from model_utils import fields
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
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

    @property
    @abstractmethod
    def updated_at(self) -> models.DateTimeField:
        pass

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=120, unique=True)
    updated_at = fields.AutoLastModifiedField()
    keywords = models.CharField(
        max_length=500,
        validators=[
            RegexValidator(
                regex="^[0-9a-zA-Z\-\s]+(,[0-9a-zA-Z\-\s]+)*$",
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

    @property
    def keyword_contains(self) -> list[str]:
        return [k for k in self.keywords.split(",") if not k.startswith("-")]

    @property
    def keyword_excludes(self) -> list[str]:
        return [
            re.search(r"-(.*)", k).group(1)
            for k in self.keywords.split(",")
            if k.startswith("-")
        ]

    def get_absolute_url(self):
        return reverse("tag_details", kwargs={"pk": self.pk})


class Company(BaseModel):
    name = models.CharField(max_length=120, unique=True, blank=True)
    updated_at = fields.AutoLastModifiedField()
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def get_absolute_url(self):
        return reverse("company_details", kwargs={"pk": self.pk})


class ExperiencePoint(BaseModel):
    content = models.TextField(max_length=5000, default="content")
    tags = models.ManyToManyField(Tag)
    updated_at = fields.AutoLastModifiedField()
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.content


def job_duty_validator(value: str) -> None:
    pattern = r"(?:(?!\s*\*).*(?:\n\s*\* .*)+)+$"
    if not bool(re.match(pattern, value, re.MULTILINE)):
        raise ValidationError(
            "You must enter list of job duties followed by one or more '*' bullet points"
        )


class ResumeJob(BaseModel):
    title = models.CharField(max_length=120)
    updated_at = fields.AutoLastModifiedField()
    company = models.CharField(max_length=120)
    company_description = models.CharField(max_length=120)
    job_duty_raw_text = models.TextField(
        max_length=5000,
        validators=[
            job_duty_validator,
        ],
    )
    start_at = models.DateField()
    end_at = models.DateField(null=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f"{self.title} at {self.company}"

    def get_absolute_url(self):
        return reverse("resume_job_details", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"


class ResumeJobDuty(BaseModel):
    title = models.CharField(max_length=120)
    experience_points = models.ManyToManyField(ExperiencePoint)
    updated_at = fields.AutoLastModifiedField()
    job = models.ForeignKey(
        ResumeJob, on_delete=models.CASCADE, related_name="job_duties"
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Job duty"
        verbose_name_plural = "Job duties"


class ResumeEducation(BaseModel):
    school = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    degree = models.CharField(max_length=120)
    updated_at = fields.AutoLastModifiedField()
    start_at_year = models.IntegerField(null=True, blank=True)
    end_at_year = models.IntegerField()
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse("resume_education_details", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.degree} - {self.school}, {self.location} ({self.end_at_year})"


class Resume(BaseModel):
    title = models.CharField(max_length=120)
    updated_at = fields.AutoLastModifiedField()
    jobs = models.ManyToManyField(ResumeJob)
    education = models.ManyToManyField(ResumeEducation)
    skills = models.TextField(max_length=1000, null=True)
    languages = models.CharField(max_length=500, null=True)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse("resume_details", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title


class JobDescription(BaseModel):
    title = models.CharField(max_length=120)
    updated_at = fields.AutoLastModifiedField()
    raw_text = models.TextField(max_length=5000, null=True)
    tags = models.ManyToManyField(Tag)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="job_descriptions"
    )
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f"{self.title} at {self.company}"

    def get_absolute_url(self):
        return reverse("job_description_details", kwargs={"pk": self.pk})


def get_tags_for(raw_text: str) -> list[Tag]:
    jd_tags = set()
    for tag in Tag.objects.all():
        for contains_pattern in tag.keyword_contains:
            if contains_pattern in raw_text.lower():
                if tag not in jd_tags:
                    jd_tags.add(tag)
        for exclude_pattern in tag.keyword_excludes:
            if exclude_pattern in raw_text.lower():
                if tag in jd_tags:
                    jd_tags.remove(tag)
    return list(jd_tags)


@receiver(post_save, sender=JobDescription)
def update_job_description_tags(sender, instance, created, **kwargs) -> None:
    if tags := get_tags_for(instance.raw_text):
        instance.tags.set(tags)


@receiver(post_save, sender=ResumeJob)
def update_resume_job_duties(sender, instance, created, **kwargs) -> None:
    instance.job_duties.all().delete()
    job_duty_bullet_point_parts = [
        b.strip() for b in instance.job_duty_raw_text.split("\n")
    ]
    job_duty_bullet_point_parts = [
        p for p in job_duty_bullet_point_parts if p != ""
    ]
    k = job_duty_bullet_point_parts[0]
    job_duty_bullet_points = {k: []}
    for part in job_duty_bullet_point_parts:
        if part.startswith("*"):
            job_duty_bullet_points[k].append(
                re.search("^\*(.+)", part).group(1).strip()
            )
        else:
            k = part
            job_duty_bullet_points.update({k: []})
    for raw_job_duty, raw_bullet_points in job_duty_bullet_points.items():
        job_duty, _ = ResumeJobDuty.objects.get_or_create(
            title=raw_job_duty, job=instance
        )
        job_duty.experience_points.clear()
        for bullet_point in raw_bullet_points:
            exp, _ = ExperiencePoint.objects.get_or_create(
                content=bullet_point
            )
            job_duty.experience_points.add(exp)
            if tags := get_tags_for(bullet_point):
                exp.tags.set(tags)
