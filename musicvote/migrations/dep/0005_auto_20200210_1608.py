# Generated by Django 3.0.3 on 2020-02-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicvote', '0004_auto_20200210_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
