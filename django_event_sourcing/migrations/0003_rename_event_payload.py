# Generated by Django 3.1.4 on 2021-01-09 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("django_event_sourcing", "0002_eventhandlerlog"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="payload",
            new_name="data",
        ),
    ]
