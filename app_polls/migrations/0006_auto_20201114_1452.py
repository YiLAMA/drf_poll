# Generated by Django 2.2.16 on 2020-11-14 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0005_auto_20201114_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Вариант ответа', 'verbose_name_plural': 'Варианты ответа'},
        ),
        migrations.AlterModelOptions(
            name='poll',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
    ]
