# Generated by Django 4.2.3 on 2023-08-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0036_alter_company_name_alter_historicalcompany_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalresumeeducation',
            name='end_at_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='historicalresumeeducation',
            name='start_at_year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resumeeducation',
            name='end_at_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='resumeeducation',
            name='start_at_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
