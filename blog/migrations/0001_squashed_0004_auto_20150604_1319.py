# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'blog', '0001_initial'), (b'blog', '0002_about_links'), (b'blog', '0003_auto_20150604_1318'), (b'blog', '0004_auto_20150604_1319')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'About Me')),
            ],
            options={
                'verbose_name_plural': 'About Me',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=127, verbose_name=b'Title')),
                ('slug', models.SlugField(unique=True, max_length=127, verbose_name=b'URL Slug')),
                ('content', models.TextField(verbose_name=b'Content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created')),
                ('display', models.BooleanField(default=False, verbose_name=b'Display on Blog?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(unique=True, max_length=63, verbose_name=b'Category')),
                ('slug', models.SlugField(unique=True, max_length=63, verbose_name=b'URL Slug')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'img', verbose_name=b'Image')),
                ('caption', models.TextField(verbose_name=b'Caption')),
                ('post', models.ForeignKey(to='blog.BlogPost')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=63, verbose_name=b'Name of Site')),
                ('link', models.URLField(verbose_name=b'Link')),
                ('about', models.ForeignKey(to='blog.About')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(to='blog.Category'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'About Me')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=63, verbose_name=b'Name of Site')),
                ('link', models.URLField(verbose_name=b'Link')),
                ('about', models.ForeignKey(to='blog.About')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
    ]
