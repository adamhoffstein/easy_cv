# Generated by Django 4.2.3 on 2023-08-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0028_remove_historicalresumeeducation_end_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalresumeeducation',
            name='end_at_year',
            field=models.IntegerField(default=12345),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalresumeeducation',
            name='start_at_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='resumeeducation',
            name='end_at_year',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resumeeducation',
            name='start_at_year',
            field=models.IntegerField(null=True),
        ),
    ]
