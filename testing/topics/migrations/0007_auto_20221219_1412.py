# Generated by Django 3.2.16 on 2022-12-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_auto_20221212_1110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id'], 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
