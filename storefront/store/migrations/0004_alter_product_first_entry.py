# Generated by Django 4.2.4 on 2023-09-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_rename_name_collection_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="first_entry",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
