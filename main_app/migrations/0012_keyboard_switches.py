# Generated by Django 4.1 on 2022-08-12 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_keyboard_switches'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyboard',
            name='switches',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to='main_app.switch'),
            preserve_default=False,
        ),
    ]