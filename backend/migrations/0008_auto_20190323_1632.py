# Generated by Django 2.1.7 on 2019-03-23 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190323_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='id_game',
        ),
        migrations.AddField(
            model_name='reservation',
            name='idgame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Game'),
        ),
    ]
