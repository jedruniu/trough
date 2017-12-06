# Generated by Django 2.0 on 2017-12-06 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(null=True)),
                ('units', models.IntegerField(choices=[(0, 'Gram')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('ingredient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='amount',
            name='ingredient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Ingredient'),
        ),
    ]