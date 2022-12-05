# Generated by Django 4.1.3 on 2022-12-05 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_series_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['position'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.AlterModelOptions(
            name='shiur',
            options={'verbose_name_plural': 'Shiurim'},
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.category', verbose_name='parent'),
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
