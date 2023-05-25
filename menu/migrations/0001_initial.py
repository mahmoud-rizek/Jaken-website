# Generated by Django 4.2.1 on 2023-05-25 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('type', models.CharField(choices=[('Drinks', 'Drinks'), ('Drip coffe', 'Drip coffe'), ('Cold coffe', 'Cold coffe'), ('Hot coffe', 'Hot coffe'), ('Extra', 'Extra'), ('Matcha', 'Matcha'), ('Sandwiches', 'Sandwiches')], max_length=100, verbose_name='Item type')),
            ],
        ),
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imges', models.ImageField(upload_to='images/', verbose_name='Images')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu', verbose_name='MenuImages')),
            ],
        ),
    ]
