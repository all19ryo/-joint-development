# Generated by Django 2.2.10 on 2020-04-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0002_auto_20200428_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='inst_link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='circle',
            name='tweet_link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]