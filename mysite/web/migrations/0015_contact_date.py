# Generated by Django 3.1.4 on 2021-01-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20210124_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
