# Generated by Django 4.2.11 on 2024-05-30 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMarketing', '0010_paqueteservicios_carritousuario_paquete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritousuario',
            name='paquete',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='paquete_carrito',
        ),
        migrations.DeleteModel(
            name='PaqueteServicios',
        ),
    ]
