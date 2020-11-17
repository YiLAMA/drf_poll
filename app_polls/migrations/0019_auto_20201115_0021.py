# Generated by Django 2.2.16 on 2020-11-15 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0018_auto_20201115_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='app_polls.Choice', verbose_name='Выбрать ответ'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice_many',
            field=models.ManyToManyField(blank=True, related_name='choice_many', to='app_polls.Choice', verbose_name='Несколько ответов'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice_text',
            field=models.CharField(max_length=100, null=True, verbose_name='Ответ текстом'),
        ),
    ]
