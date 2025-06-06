# Generated by Django 5.2 on 2025-06-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Obra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=105)),
                ('apellido', models.CharField(max_length=105)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='artistas')),
                ('biografia', models.FileField(blank=True, null=True, upload_to='artistas')),
                ('obra', models.ManyToManyField(blank=True, to='Obra.obra')),
            ],
        ),
    ]
