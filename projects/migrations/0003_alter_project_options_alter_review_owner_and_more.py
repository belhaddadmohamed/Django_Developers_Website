# Generated by Django 4.2.4 on 2023-08-27 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_bio"),
        ("projects", "0002_project_owner_review_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["created"]},
        ),
        migrations.AlterField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("owner", "project")},
        ),
    ]
