# Generated by Django 4.2.3 on 2023-08-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cv", "0035_alter_resume_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="name",
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name="historicalcompany",
            name="name",
            field=models.CharField(db_index=True, max_length=120),
        ),
    ]
