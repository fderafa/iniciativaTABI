# Generated by Django 4.1.7 on 2023-03-31 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGET_crawler', '0009_alter_tnextcrawlerexecute_lastexecute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tnextcrawlerexecute',
            name='lastExecute',
            field=models.DateTimeField(),
        ),
    ]