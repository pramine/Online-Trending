# Generated by Django 2.1.7 on 2019-03-30 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0020_story_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Story', verbose_name='story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'bookmark_article',
            },
        ),
    ]