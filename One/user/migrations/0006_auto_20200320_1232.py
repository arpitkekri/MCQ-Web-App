# Generated by Django 3.0.4 on 2020-03-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200320_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='created_on',
        ),
        migrations.AddField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
