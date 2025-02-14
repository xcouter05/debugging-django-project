# Generated by Django 4.2 on 2025-02-12 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc1', models.TextField()),
                ('desc2', models.TextField()),
                ('img1', models.ImageField(default='default.png', upload_to='portfolio')),
                ('img2', models.ImageField(default='default.png', upload_to='portfolio')),
                ('img3', models.ImageField(default='default.png', upload_to='portfolio')),
                ('project_url', models.CharField(max_length=70)),
                ('client', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.category')),
            ],
        ),
    ]
