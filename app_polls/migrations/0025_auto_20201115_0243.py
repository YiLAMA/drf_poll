# Generated by Django 2.2.16 on 2020-11-15 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0024_auto_20201115_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice_many',
            field=models.ManyToManyField(blank=True, related_name='choice_many', to='app_polls.Choice', verbose_name='Несколько ответов'),
        ),
    ]
