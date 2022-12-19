# Generated by Django 3.2.16 on 2022-12-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0007_auto_20221219_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='votes',
            new_name='right_answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='wrong_answers',
            field=models.IntegerField(default=0),
        ),
    ]