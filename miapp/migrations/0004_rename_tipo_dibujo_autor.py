# Generated by Django 5.0.3 on 2024-03-29 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_alter_carta_tipo_alter_dibujo_tipo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dibujo',
            old_name='tipo',
            new_name='autor',
        ),
    ]