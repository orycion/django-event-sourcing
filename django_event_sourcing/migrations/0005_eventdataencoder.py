# Generated by Django 3.1.4 on 2021-02-14 11:28

from django.db import migrations, models
import django_event_sourcing.models


class Migration(migrations.Migration):

    dependencies = [
        ("django_event_sourcing", "0004_eventsideeffectlog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="data",
            field=models.JSONField(
                encoder=django_event_sourcing.models.ModelJSONEncoder
            ),
        ),
    ]
