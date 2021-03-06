# Generated by Django 2.2.16 on 2020-11-15 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_polls', '0017_auto_20201115_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='app_polls.Choice', verbose_name='Ответ текстом'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice_many',
            field=models.ManyToManyField(blank=True, related_name='choice_many', to='app_polls.Choice', verbose_name='Выбрать ответ'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice_text',
            field=models.CharField(max_length=200, null=True, verbose_name='Выбрать несколько'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='app_polls.Poll', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='app_polls.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_id',
            field=models.IntegerField(help_text='Уникальный номер пользователя', verbose_name='ID пользователя'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_name',
            field=models.CharField(default='Аноним', help_text='Не более 50 символов', max_length=50, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(help_text='Укажите, когда перестанет быть активным опрос', verbose_name='Время окончания опроса'),
        ),
    ]
