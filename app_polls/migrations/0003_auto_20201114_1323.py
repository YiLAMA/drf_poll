# Generated by Django 2.2.16 on 2020-11-14 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0002_auto_20201114_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='poll_name',
            new_name='name',
        ),
    ]