# Generated by Django 4.2.3 on 2023-08-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0027_alter_historicalresumeeducation_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalresumeeducation',
            name='end_at',
        ),
        migrations.RemoveField(
            model_name='historicalresumeeducation',
            name='start_at',
        ),
        migrations.RemoveField(
            model_name='resumeeducation',
            name='end_at',
        ),
        migrations.RemoveField(
            model_name='resumeeducation',
            name='start_at',
        ),
        migrations.AddField(
            model_name='historicalresumeeducation',
            name='end_at_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='historicalresumeeducation',
            name='start_at_year',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumeeducation',
            name='end_at_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='resumeeducation',
            name='start_at_year',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
    ]
