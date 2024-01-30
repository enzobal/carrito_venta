# Generated by Django 4.2.5 on 2024-01-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarritoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos3/')),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
