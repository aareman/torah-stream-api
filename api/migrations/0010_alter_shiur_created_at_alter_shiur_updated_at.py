# Generated by Django 4.1.3 on 2022-12-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_shiur_imported_series_shiur_imported_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiur',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shiur',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]