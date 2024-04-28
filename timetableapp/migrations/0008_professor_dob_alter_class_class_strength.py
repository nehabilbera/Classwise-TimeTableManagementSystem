# Generated by Django 5.0.4 on 2024-04-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetableapp', '0007_remove_professor_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='dob',
            field=models.DateField(default='2024-04-21'),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_strength',
            field=models.IntegerField(default=100, null=True),
        ),
    ]