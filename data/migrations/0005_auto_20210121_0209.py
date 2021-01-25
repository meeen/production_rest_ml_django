# Generated by Django 2.2.17 on 2021-01-21 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_machine_domain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='api_key',
        ),
        migrations.AlterField(
            model_name='machine',
            name='domain',
            field=models.SlugField(unique=True),
        ),
    ]
