# Generated by Django 4.2.6 on 2023-11-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_departamento_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EPS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=80)),
            ],
        ),
    ]