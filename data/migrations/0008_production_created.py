# Generated by Django 2.2.17 on 2021-01-21 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_remove_production_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]