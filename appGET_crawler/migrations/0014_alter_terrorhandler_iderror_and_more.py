# Generated by Django 4.1.7 on 2023-04-02 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGET_crawler', '0013_alter_terrorhandler_iderror_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terrorhandler',
            name='idError',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tnextcrawlerexecute',
            name='idNext',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]