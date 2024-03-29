# Generated by Django 5.0.1 on 2024-01-29 23:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('desde', models.TimeField()),
                ('hasta', models.TimeField()),
                ('todo_el_dia', models.BooleanField(default=False)),
                ('lugar', models.CharField(max_length=100)),
                ('cupos', models.IntegerField(default=0)),
                ('cupos_maximos', models.IntegerField(default=0)),
                ('cupos_ilimitados', models.BooleanField(default=False)),
                ('precio', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='eventos_aguadas/')),
                ('adicional', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
