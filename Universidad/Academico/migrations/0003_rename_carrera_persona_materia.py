# Generated by Django 5.0.4 on 2024-05-06 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_persona_delete_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='Carrera',
            new_name='materia',
        ),
    ]
