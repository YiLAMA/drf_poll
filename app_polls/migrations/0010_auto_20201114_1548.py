# Generated by Django 2.2.16 on 2020-11-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0009_answer_choice_many'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice_many',
            field=models.ManyToManyField(blank=True, related_name='choice_many', to='app_polls.Choice'),
        ),
    ]
