# Generated by Django 2.2.16 on 2022-04-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20220415_1334'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='uniq_follow',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='follow'),
        ),
    ]
