# Generated by Django 3.2.4 on 2021-11-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
