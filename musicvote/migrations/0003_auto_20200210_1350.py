# Generated by Django 3.0.3 on 2020-02-10 12:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicvote', '0002_auto_20200210_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='musicvote.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'song'), name='rating by user'),
        ),
    ]
