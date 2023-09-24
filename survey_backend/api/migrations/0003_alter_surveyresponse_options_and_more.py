# Generated by Django 4.2 on 2023-09-23 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_survey_isclosed_surveyresponse_time_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="surveyresponse",
            options={"ordering": ("-date",), "verbose_name_plural": "Survey Response"},
        ),
        migrations.RemoveField(model_name="survey", name="max_length",),
        migrations.RemoveField(model_name="survey", name="max_value",),
        migrations.RemoveField(model_name="survey", name="min_value",),
    ]