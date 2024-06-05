# Generated by Django 5.0.4 on 2024-05-08 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_rename_groupmodel_group_student_delete_studentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='album_number',
            field=models.IntegerField(default=724345, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.group'),
        ),
    ]
