# Generated by Django 3.1.4 on 2021-01-23 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_contact_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
