# Generated by Django 4.2.3 on 2023-08-10 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_started', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_started', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.topic')),
            ],
        ),
    ]
