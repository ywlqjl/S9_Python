# Generated by Django 2.1.2 on 2018-11-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp7_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='address',
            field=models.CharField(max_length=500),
        ),
    ]