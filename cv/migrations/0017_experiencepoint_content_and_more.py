# Generated by Django 4.2.3 on 2023-08-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0016_historicalresumejob_updated_at_resumejob_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencepoint',
            name='content',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='historicalexperiencepoint',
            name='content',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]