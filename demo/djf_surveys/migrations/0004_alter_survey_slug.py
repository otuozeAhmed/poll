# Generated by Django 4.2.1 on 2023-10-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djf_surveys", "0003_alter_question_label"),
    ]

    operations = [
        migrations.AlterField(
            model_name="survey",
            name="slug",
            field=models.SlugField(default="", max_length=900, verbose_name="slug"),
        ),
    ]
