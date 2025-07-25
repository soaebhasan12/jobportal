# Generated by Django 5.1.7 on 2025-07-24 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employer", "0009_alter_jobs_location_alter_jobs_qualification"),
        ("jobapp", "0005_alter_employer_regdate"),
        ("jsapp", "0005_alter_appliedjobs_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="response",
            name="emailaddress",
            field=models.EmailField(max_length=50),
        ),
        migrations.CreateModel(
            name="SavedJob",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("saved_at", models.DateTimeField(auto_now_add=True)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="employer.jobs"
                    ),
                ),
                (
                    "jobseeker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobapp.jobseeker",
                    ),
                ),
            ],
            options={
                "unique_together": {("jobseeker", "job")},
            },
        ),
    ]
