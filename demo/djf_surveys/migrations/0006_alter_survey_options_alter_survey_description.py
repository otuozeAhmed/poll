# Generated by Django 4.2.1 on 2023-10-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djf_surveys", "0005_alter_question_key"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="survey",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="survey",
            name="description",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="description"
            ),
        ),
    ]