# Generated by Django 2.1.7 on 2019-03-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id_entity',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='id_game',
            field=models.IntegerField(auto_created=True),
        ),
    ]
