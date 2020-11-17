# Generated by Django 2.2.16 on 2020-11-14 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0011_auto_20201114_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='app_polls.Poll', verbose_name='Опросник'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Т', 'ответ текстом'), ('О', 'один ответ'), ('М', 'много ответов')], help_text='Выберите какой тип ответа нужен для этого вопроса', max_length=10, verbose_name='Тип вопроса'),
        ),
    ]
