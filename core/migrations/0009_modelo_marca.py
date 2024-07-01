# Generated by Django 5.0.2 on 2024-07-01 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_modelo_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelo",
            name="marca",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modelos",
                to="core.marca",
            ),
        ),
    ]
