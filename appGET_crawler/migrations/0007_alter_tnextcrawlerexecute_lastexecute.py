# Generated by Django 4.1.7 on 2023-03-31 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGET_crawler', '0006_alter_tnextcrawlerexecute_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tnextcrawlerexecute',
            name='lastExecute',
            field=models.DateTimeField(),
        ),
    ]