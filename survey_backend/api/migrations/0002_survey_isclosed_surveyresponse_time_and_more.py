# Generated by Django 4.2 on 2023-09-23 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="isClosed",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="surveyresponse",
            name="time",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="surveyresponse",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="survey",
            name="isActive",
            field=models.BooleanField(default=False),
        ),
    ]
