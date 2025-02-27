# Generated by Django 5.1.1 on 2024-12-17 16:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_alter_subtopic_name_alter_test_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coding_skills', models.FloatField(blank=True, null=True)),
                ('aptitude_skills', models.FloatField(blank=True, null=True)),
                ('verbal_skills', models.FloatField(blank=True, null=True)),
                ('placement_pred', models.BooleanField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserScore', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
