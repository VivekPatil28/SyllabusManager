# Generated by Django 4.2.3 on 2023-08-14 08:15

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0004_alter_useranswer_selected_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='user_stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_coverage', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('syllabus_coverage_time', models.DecimalField(decimal_places=5, default=0, max_digits=7)),
                ('test_score', models.PositiveIntegerField(default=0)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_stats', to='Main.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
