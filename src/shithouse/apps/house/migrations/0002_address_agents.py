# Generated by Django 5.0.6 on 2024-06-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agency", "0001_initial"),
        ("house", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="agents",
            field=models.ManyToManyField(to="agency.agent"),
        ),
    ]