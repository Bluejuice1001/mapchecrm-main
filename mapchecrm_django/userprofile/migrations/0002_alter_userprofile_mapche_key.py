# Generated by Django 4.1.3 on 2022-11-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mapche_key',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
