# Generated by Django 2.1.7 on 2019-03-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20190323_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='popularity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
