# Generated by Django 3.1.4 on 2021-01-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20210124_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='NoName', max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='NoName', max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]