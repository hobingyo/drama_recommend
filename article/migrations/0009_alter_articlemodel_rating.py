# Generated by Django 4.0.4 on 2022-06-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_rename_tweet_articlecomment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='rating',
            field=models.FloatField(),
        ),
    ]