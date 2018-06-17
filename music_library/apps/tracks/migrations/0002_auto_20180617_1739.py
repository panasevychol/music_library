# Generated by Django 2.0.6 on 2018-06-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='playlink',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='popularity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
