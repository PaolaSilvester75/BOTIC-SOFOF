# Generated by Django 5.1.4 on 2024-12-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_agregacion_de_relacion_y_campos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='f_vencimiento',
            field=models.DateField(),
        ),
    ]