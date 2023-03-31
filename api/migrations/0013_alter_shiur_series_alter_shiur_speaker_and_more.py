# Generated by Django 4.1.3 on 2023-03-31 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_shiur_options_rename_track_shiur_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiur',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shiurim', to='api.series'),
        ),
        migrations.AlterField(
            model_name='shiur',
            name='speaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.speaker'),
        ),
        migrations.AlterField(
            model_name='shiur',
            name='video_src',
            field=models.URLField(blank=True, null=True),
        ),
    ]