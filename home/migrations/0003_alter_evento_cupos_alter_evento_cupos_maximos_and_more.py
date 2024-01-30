# Generated by Django 5.0.1 on 2024-01-30 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_evento_fecha_alter_evento_organizador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='cupos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='cupos_maximos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='desde',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hasta',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='precio',
            field=models.CharField(blank=True, default='Gratuito', max_length=100, null=True),
        ),
    ]