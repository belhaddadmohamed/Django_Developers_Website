# Generated by Django 4.2.4 on 2023-08-27 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_bio"),
        ("projects", "0003_alter_project_options_alter_review_owner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]
