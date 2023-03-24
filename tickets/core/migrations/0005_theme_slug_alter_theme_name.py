# Generated by Django 4.1.7 on 2023-03-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_answer_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, null=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Тематика теста'),
        ),
    ]
