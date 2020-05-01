# Generated by Django 2.2.10 on 2020-04-28 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='circle',
            old_name='link',
            new_name='tweet_link',
        ),
        migrations.AddField(
            model_name='circle',
            name='inst_link',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='types',
            field=models.CharField(default='スポーツ系', max_length=50),
            preserve_default=False,
        ),
    ]
