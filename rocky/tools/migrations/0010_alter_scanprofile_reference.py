# Generated by Django 3.2.5 on 2021-12-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tools", "0009_scanprofile_is_source_ooi"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scanprofile",
            name="reference",
            field=models.TextField(),
        ),
    ]
