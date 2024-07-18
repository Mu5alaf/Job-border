# Generated by Django 5.0.7 on 2024-07-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(blank=True, choices=[('Full time', 'Full Time'), ('Part time', 'Part Time')], max_length=15),
        ),
    ]
