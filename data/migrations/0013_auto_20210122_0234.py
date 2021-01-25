# Generated by Django 2.2.17 on 2021-01-22 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20210122_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_typ',
            name='time',
            field=models.FloatField(default=10),
        ),
        migrations.CreateModel(
            name='tool_change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.machine')),
            ],
        ),
    ]