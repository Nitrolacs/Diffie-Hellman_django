# Generated by Django 4.1.10 on 2023-12-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0006_remove_profile_salt"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                ("image", models.ImageField(upload_to="users/%Y/%m/%d/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="profile",
            name="photo",
        ),
        migrations.AddField(
            model_name="profile",
            name="photos",
            field=models.ManyToManyField(blank=True, to="account.photo"),
        ),
    ]
