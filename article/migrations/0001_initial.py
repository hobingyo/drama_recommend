# Generated by Django 4.0.4 on 2022-06-02 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('synopsis', models.CharField(max_length=256)),
                ('genre', models.CharField(max_length=256)),
                ('tags', models.CharField(max_length=256)),
                ('cast', models.CharField(max_length=256)),
                ('rating', models.IntegerField()),
                ('aired_date', models.DateTimeField()),
                ('episode', models.IntegerField()),
                ('Aged', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
