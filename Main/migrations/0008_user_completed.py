# Generated by Django 4.2.3 on 2023-08-16 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0007_semester_subject_sem'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_topics', to='Main.subtopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_completed_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
