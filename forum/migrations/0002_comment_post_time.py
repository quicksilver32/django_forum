# Generated by Django 3.1 on 2020-08-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_time',
            field=models.DateTimeField(null=True),
        ),
    ]