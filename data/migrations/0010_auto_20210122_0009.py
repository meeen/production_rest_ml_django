# Generated by Django 2.2.17 on 2021-01-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_production_machinetime'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mlmodels',
        ),
        migrations.AddField(
            model_name='machine',
            name='model',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]