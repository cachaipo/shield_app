# Generated by Django 3.0.6 on 2020-05-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0007_metahuman_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True),
        ),
    ]
