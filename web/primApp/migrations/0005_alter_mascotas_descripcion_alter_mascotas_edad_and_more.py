# Generated by Django 4.0.5 on 2022-08-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primApp', '0004_alter_mascotas_descripcion_alter_mascotas_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='descripcion',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='edad',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='vacunas',
            field=models.TextField(max_length=150),
        ),
    ]
