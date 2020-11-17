# Generated by Django 2.2.16 on 2020-11-15 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0020_auto_20201115_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='choice_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice_one', to='app_polls.Choice', verbose_name='Выбрать ответ'),
        ),
    ]