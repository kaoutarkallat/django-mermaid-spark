# Generated by Django 3.2.12 on 2022-09-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220918_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('accessories', 'accessories'), ('bras', 'bras'), ('leggings', 'leggings'), ('shorts', 'shorts'), ('sneakers', 'sneakers'), ('tank_tops', 'tank_tops')], db_index=True, max_length=10000, null=True),
        ),
    ]
