# Generated by Django 4.2.7 on 2023-12-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_pacientes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paciente",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
