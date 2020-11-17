# Generated by Django 2.2.16 on 2020-11-15 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0023_auto_20201115_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice_many',
            field=models.ManyToManyField(blank=True, null=True, related_name='choice_many', to='app_polls.Choice', verbose_name='Несколько ответов'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_polls.Choice', verbose_name='Выбрать ответ'),
        ),
    ]
