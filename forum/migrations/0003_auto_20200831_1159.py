# Generated by Django 3.1 on 2020-08-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_comment_post_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['post_time']},
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(help_text='Введите название темы', max_length=200, unique=True),
        ),
    ]