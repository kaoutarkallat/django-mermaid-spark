# Generated by Django 3.2.12 on 2022-09-18 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220918_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('rank', models.IntegerField(blank=True, db_index=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('accessories', 'accessories'), ('bras', 'bras'), ('leggings', 'leggings'), ('shorts', 'shorts'), ('sneakers', 'sneakers'), ('tank_tops', 'tank_tops')], db_index=True, max_length=10000, null=True)),
                ('url', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('img_front', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('img_back', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('price', models.CharField(blank=True, max_length=10000, null=True)),
                ('oldprice', models.CharField(blank=True, max_length=10000, null=True)),
                ('star', models.IntegerField(blank=True, default=5, null=True)),
                ('Reviews', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('long_description', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'history_product',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
