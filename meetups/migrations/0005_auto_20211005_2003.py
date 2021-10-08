# Generated by Django 3.2.7 on 2021-10-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_auto_20211004_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.EmailField(default='12-12-2020', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]