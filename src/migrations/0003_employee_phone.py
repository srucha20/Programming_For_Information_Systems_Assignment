# Generated by Django 3.2 on 2022-12-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20221213_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default='emty', max_length=20),
            preserve_default=False,
        ),
    ]