# Generated by Django 4.0.4 on 2022-06-07 07:17

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('article', '0009_alter_articlemodel_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='tags',
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
