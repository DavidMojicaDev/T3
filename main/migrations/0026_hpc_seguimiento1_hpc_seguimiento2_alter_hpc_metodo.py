# Generated by Django 4.2.6 on 2023-11-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_rename_conductas_sex_resgo_hpc_conductas_sex_riesgo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hpc',
            name='seguimiento1',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='hpc',
            name='seguimiento2',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='hpc',
            name='metodo',
            field=models.TextField(max_length=300, null=True),
        ),
    ]