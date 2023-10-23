# Generated by Django 4.2.1 on 2023-10-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customuser", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="last_name",
        ),
        migrations.AddField(
            model_name="customuser",
            name="full_name",
            field=models.CharField(default="", max_length=50),
        ),
    ]