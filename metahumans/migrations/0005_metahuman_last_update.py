# Generated by Django 3.0.5 on 2020-05-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0004_metahuman_ally'),
    ]

    operations = [
        migrations.AddField(
            model_name='metahuman',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
