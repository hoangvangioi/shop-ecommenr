# Generated by Django 4.0.2 on 2022-02-24 15:38

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='TeamAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('featured_image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('post_views', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_1', models.CharField(max_length=1000)),
                ('about_2', models.CharField(max_length=1000)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.teamabout')),
            ],
        ),
    ]