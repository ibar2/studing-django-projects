# Generated by Django 4.1.4 on 2023-07-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0004_meaw"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
