# Generated by Django 4.2.4 on 2023-08-28 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_message"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="name",
            new_name="name_sender",
        ),
    ]
