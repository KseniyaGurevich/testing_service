# Generated by Django 3.2.16 on 2022-12-19 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0010_auto_20221219_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testquestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='test',
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
        migrations.DeleteModel(
            name='TestQuestion',
        ),
    ]
