# Generated by Django 2.2.16 on 2020-11-15 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0021_auto_20201115_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user_id',
            field=models.PositiveSmallIntegerField(help_text='Уникальный номер пользователя', verbose_name='ID пользователя'),
        ),
    ]