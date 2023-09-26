# Generated by Django 4.0 on 2023-09-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=255)),
                ('Descripcion', models.TextField()),
                ('Lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('Lng', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]