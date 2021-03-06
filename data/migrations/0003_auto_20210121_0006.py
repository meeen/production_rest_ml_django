# Generated by Django 2.2.17 on 2021-01-20 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210120_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='machine_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manu', models.CharField(max_length=64)),
                ('modell', models.CharField(max_length=64)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='mtype',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.machine_type'),
        ),
    ]
