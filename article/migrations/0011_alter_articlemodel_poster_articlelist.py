# Generated by Django 4.0.5 on 2022-06-10 05:53

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('article', '0010_remove_articlemodel_tags_articlemodel_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='poster',
            field=models.FileField(upload_to='Uploaded_Files/'),
        ),
        migrations.CreateModel(
            name='ArticleList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('synopsis', models.CharField(max_length=256)),
                ('genre', models.CharField(max_length=256)),
                ('cast', models.CharField(max_length=256)),
                ('rating', models.FloatField()),
                ('episode', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'db_table': 'article_list',
            },
        ),
    ]