# Generated by Django 5.0.4 on 2024-05-16 18:38

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0008_alter_scheduledlecture_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('present', models.BooleanField(default=False)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.scheduledlecture')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.student')),
            ],
        ),
    ]