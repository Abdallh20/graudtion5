# Generated by Django 5.1.2 on 2024-10-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstapi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="images",
            field=models.CharField(default="", max_length=10000),
        ),
    ]