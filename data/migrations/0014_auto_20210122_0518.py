# Generated by Django 2.2.17 on 2021-01-22 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20210122_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='mtype',
        ),
        migrations.AddField(
            model_name='machine',
            name='manu',
            field=models.CharField(default='Haddad', max_length=64),
        ),
        migrations.AddField(
            model_name='machine',
            name='modell',
            field=models.CharField(default='Ultradreher', max_length=64),
        ),
        migrations.AddField(
            model_name='machine',
            name='year',
            field=models.IntegerField(default=2016),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.product_typ'),
        ),
        migrations.DeleteModel(
            name='machine_type',
        ),
    ]
