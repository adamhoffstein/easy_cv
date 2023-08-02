# Generated by Django 4.2.3 on 2023-07-31 02:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv', '0002_remove_resume_just_created_tag_historicaltag_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExperiencePoint',
            new_name='Experience',
        ),
        migrations.RenameModel(
            old_name='HistoricalExperiencePoint',
            new_name='HistoricalExperience',
        ),
        migrations.AlterModelOptions(
            name='historicalexperience',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical experience', 'verbose_name_plural': 'historical experiences'},
        ),
    ]
