# Generated by Django 3.0.4 on 2020-03-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_marks_scored_total_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='number_of_questions',
            field=models.IntegerField(default=1),
        ),
    ]