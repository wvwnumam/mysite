# Generated by Django 2.2.12 on 2020-08-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200817_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
