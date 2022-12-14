# Generated by Django 3.2 on 2022-12-16 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_employee_profile_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_shift',
            old_name='end_date',
            new_name='d_date',
        ),
        migrations.RemoveField(
            model_name='employee_shift',
            name='start_date',
        ),
        migrations.AddField(
            model_name='employee_shift',
            name='end_time',
            field=models.CharField(default='5', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_shift',
            name='start_time',
            field=models.CharField(default='5', max_length=10),
            preserve_default=False,
        ),
    ]
