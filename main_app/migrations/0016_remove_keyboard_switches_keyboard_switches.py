# Generated by Django 4.1 on 2022-08-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_keyboard_switches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyboard',
            name='switches',
        ),
        migrations.AddField(
            model_name='keyboard',
            name='switches',
            field=models.ManyToManyField(to='main_app.switch'),
        ),
    ]
