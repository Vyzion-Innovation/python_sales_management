# Generated by Django 4.2.20 on 2025-04-15 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_country_module', '0001_initial'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='country',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='common_country_module.country'),
            preserve_default=False,
        ),
    ]
