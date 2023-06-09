# Generated by Django 4.1.7 on 2023-04-01 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGET_crawler', '0010_alter_tnextcrawlerexecute_lastexecute'),
    ]

    operations = [
        migrations.CreateModel(
            name='tAccess',
            fields=[
                ('idAccess', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('accessJSON', models.JSONField()),
                ('insertDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'tAccess',
            },
        ),
        migrations.CreateModel(
            name='tErrorHandler',
            fields=[
                ('idError', models.BigAutoField(default=0, primary_key=True, serialize=False)),
                ('request', models.CharField(max_length=255)),
                ('exceptionError', models.CharField(max_length=800)),
                ('insertDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'tErrorHandler',
            },
        ),
        migrations.RenameField(
            model_name='tguests',
            old_name='GuestJson',
            new_name='guestJson',
        ),
        migrations.RemoveField(
            model_name='tguests',
            name='CPF',
        ),
        migrations.RemoveField(
            model_name='tguests',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tnextcrawlerexecute',
            name='id',
        ),
        migrations.AddField(
            model_name='tguests',
            name='insertDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tnextcrawlerexecute',
            name='idNext',
            field=models.BigAutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='tguests',
            table='tGuests',
        ),
        migrations.AlterModelTable(
            name='tnextcrawlerexecute',
            table='tNextcrawlerexecute',
        ),
        migrations.AddField(
            model_name='tguests',
            name='cpf',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
