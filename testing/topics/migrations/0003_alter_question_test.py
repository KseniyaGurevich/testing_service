# Generated by Django 3.2.16 on 2022-12-12 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20221212_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions_in_test', to='topics.test'),
        ),
    ]
