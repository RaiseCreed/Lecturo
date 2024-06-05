# Generated by Django 5.0.4 on 2024-06-01 16:00

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0010_alter_attendance_present_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('recipent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel.student')),
            ],
        ),
    ]