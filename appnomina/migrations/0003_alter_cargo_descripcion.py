# Generated by Django 4.0.3 on 2022-03-18 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0002_alter_cargo_options_alter_departamento_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
