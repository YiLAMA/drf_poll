# Generated by Django 2.2.16 on 2020-11-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0006_auto_20201114_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user_name',
            field=models.CharField(default='Аноним', max_length=50, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice_text',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
