# Generated by Django 4.1.3 on 2022-11-28 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formatted_address', models.CharField(max_length=255)),
                ('location_lat', models.FloatField()),
                ('location_lng', models.FloatField()),
                ('place_id', models.CharField(max_length=255)),
                ('address_component_nr', models.CharField(blank=True, max_length=6, null=True)),
                ('address_component_street', models.CharField(blank=True, max_length=85, null=True)),
                ('address_component_suburb', models.CharField(blank=True, max_length=58, null=True)),
                ('address_component_town', models.CharField(blank=True, max_length=58, null=True)),
                ('address_component_metro', models.CharField(blank=True, max_length=255, null=True)),
                ('address_component_province', models.CharField(blank=True, max_length=58, null=True)),
                ('address_component_province_short', models.CharField(blank=True, max_length=4, null=True)),
                ('address_component_country', models.CharField(blank=True, max_length=58, null=True)),
                ('address_component_country_short', models.CharField(blank=True, max_length=4, null=True)),
                ('address_component_postal_code', models.CharField(blank=True, max_length=8, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('mapche_key', models.CharField(blank=True, max_length=36, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='searches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
