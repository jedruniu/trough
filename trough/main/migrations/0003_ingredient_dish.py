# Generated by Django 2.0 on 2017-12-04 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='dish',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Dish'),
        ),
    ]
