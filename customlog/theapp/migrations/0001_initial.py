# Generated by Django 4.1.4 on 2023-06-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="customUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=55, unique=True)),
                ("full_name", models.CharField(max_length=100)),
                ("address", models.CharField(blank=True, max_length=130, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
