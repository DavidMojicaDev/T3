# Generated by Django 4.2.6 on 2023-12-31 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_infomiembros_id_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psillamadas',
            name='id_psicologo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main.infomiembros'),
        ),
    ]
