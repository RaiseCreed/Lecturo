# Generated by Django 5.0.4 on 2024-05-12 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_lecture_scheduledlecture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lecture',
            new_name='Subject',
        ),
    ]