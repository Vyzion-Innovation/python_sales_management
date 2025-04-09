# Generated by Django 4.2.20 on 2025-04-09 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_country_module', '0001_initial'),
        ('accounts', '0002_alter_salesuser_options_remove_salesuser_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesuser',
            name='category',
        ),
        migrations.AddField(
            model_name='salesuser',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_country_module.country'),
        ),
    ]
