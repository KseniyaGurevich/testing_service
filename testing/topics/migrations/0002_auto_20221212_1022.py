# Generated by Django 3.2.16 on 2022-12-12 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions_in_test', to='topics.group'),
        ),
    ]
