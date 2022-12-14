# Generated by Django 3.2.12 on 2022-09-25 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('REQUEST_METHOD', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('PATH_INFO', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('QUERY_STRING', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('REMOTE_ADDR', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('CONTENT_TYPE', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('HTTP_HOST', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('HTTP_CONNECTION', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('HTTP_CACHE_CONTROL', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('HTTP_SEC_CH_UA', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('HTTP_SEC_CH_UA_MOBILE', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('HTTP_SEC_CH_UA_PLATFORM', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('HTTP_UPGRADE_INSECURE_REQUESTS', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('HTTP_USER_AGENT', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'request',
            },
        ),
    ]
