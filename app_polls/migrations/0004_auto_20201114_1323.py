# Generated by Django 2.2.16 on 2020-11-14 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0003_auto_20201114_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='name',
            new_name='poll_name',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='start_date',
            new_name='pub_date',
        ),
    ]