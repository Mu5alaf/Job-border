# Generated by Django 5.0.7 on 2024-07-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_job_slug_alter_job_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('portfolio_url', models.URLField(blank=True, null=True)),
                ('cover_letter', models.TextField(blank=True, max_length=340, null=True)),
                ('cv_upload', models.FileField(blank=True, max_length=340, null=True, upload_to='apply/')),
            ],
        ),
    ]
