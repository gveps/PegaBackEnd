# Generated by Django 2.1.7 on 2019-03-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190323_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='id_entity',
        ),
        migrations.AddField(
            model_name='game',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
