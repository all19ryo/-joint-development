# Generated by Django 2.2.10 on 2020-04-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0003_auto_20200428_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='inst_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='circle',
            name='tweet_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
