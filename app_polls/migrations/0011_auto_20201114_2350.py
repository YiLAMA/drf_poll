# Generated by Django 2.2.16 on 2020-11-14 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0010_auto_20201114_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='app_polls.Poll', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Т', 'текст'), ('О', 'один'), ('М', 'много')], max_length=10, verbose_name='Тип вопроса'),
        ),
    ]
