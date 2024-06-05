# Generated by Django 5.0.4 on 2024-05-12 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_rename_name_group_group_number_group_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='album_number',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
