# Generated by Django 3.2 on 2022-12-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
