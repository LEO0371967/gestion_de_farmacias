# Generated by Django 3.2 on 2021-11-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuarios', '0002_recetas_cronico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='cronico',
            field=models.BooleanField(default=False, null=True),
        ),
    ]