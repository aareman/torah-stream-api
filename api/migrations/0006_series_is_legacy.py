# Generated by Django 4.1.3 on 2022-12-05 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_shiur_options_alter_shiur_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='is_legacy',
            field=models.BooleanField(default=False),
        ),
    ]
