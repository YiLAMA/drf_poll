# Generated by Django 2.2.16 on 2020-11-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0008_auto_20201114_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='choice_many',
            field=models.ManyToManyField(related_name='choice_many', to='app_polls.Choice'),
        ),
    ]