# Generated by Django 4.2.1 on 2023-10-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customuser", "0002_remove_customuser_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="department",
            field=models.CharField(help_text="e.g PM", max_length=15),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="staff_id",
            field=models.CharField(
                help_text="e.g 01234 or CP1234", max_length=15, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="unit",
            field=models.CharField(help_text="e.g PMT", max_length=15),
        ),
    ]
