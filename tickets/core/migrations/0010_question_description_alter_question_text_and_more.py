# Generated by Django 4.1.7 on 2023-03-22 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_question_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Пояснение к вопросу'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=250, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.theme', verbose_name='Тема вопроса'),
        ),
        migrations.AlterField(
            model_name='question',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ticket', verbose_name='Билет'),
        ),
    ]
