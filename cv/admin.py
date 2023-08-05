from django.contrib import admin

from .models import (
    Resume,
    ResumeJob,
    ResumeJobDuty,
    Tag,
    ExperiencePoint,
    Company,
    JobDescription,
)


class BaseAdmin(admin.ModelAdmin):
    exclude = ["created_by", "last_edited_by"]


@admin.register(Resume)
class ResumeAdmin(BaseAdmin):
    list_display = ["title", "created_at", "updated_at"]


@admin.register(ResumeJob)
class ResumeJobAdmin(BaseAdmin):
    list_display = ["title", "created_at", "updated_at"]


@admin.register(ResumeJobDuty)
class ResumeJobDutyAdmin(BaseAdmin):
    list_display = ["title", "created_at", "updated_at"]


@admin.register(Tag)
class TagAdmin(BaseAdmin):
    list_display = ["name", "created_at", "updated_at"]


@admin.register(ExperiencePoint)
class ExperiencePointAdmin(BaseAdmin):
    list_display = ["content", "created_at", "updated_at"]


@admin.register(Company)
class CompanyAdmin(BaseAdmin):
    list_display = ["name", "created_at", "updated_at"]


@admin.register(JobDescription)
class JobDescriptionAdmin(BaseAdmin):
    list_display = ["title", "created_at", "updated_at"]
