# Generated by Django 4.2.3 on 2023-08-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0026_historicalresumeeducation_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalresumeeducation',
            name='location',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='resumeeducation',
            name='location',
            field=models.CharField(max_length=120),
        ),
    ]