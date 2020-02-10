# Generated by Django 3.0.3 on 2020-02-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicvote', '0007_auto_20200207_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default='abcde', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default='abcde', unique=True),
            preserve_default=False,
        ),
    ]