# Generated by Django 3.1.4 on 2021-01-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20201230_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='docs',
        ),
        migrations.AddField(
            model_name='contact',
            name='file',
            field=models.FileField(default=None, upload_to='Pictures/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]
