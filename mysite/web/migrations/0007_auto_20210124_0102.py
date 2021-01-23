# Generated by Django 3.1.4 on 2021-01-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20210124_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=122, null=True),
        ),
    ]
