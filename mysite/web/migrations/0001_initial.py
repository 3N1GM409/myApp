# Generated by Django 3.1.4 on 2020-12-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=122)),
                ('last_name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=122)),
                ('docs', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
