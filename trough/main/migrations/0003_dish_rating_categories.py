# Generated by Django 2.0 on 2017-12-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_rating_name'),
        ('main', '0002_add_choices_to_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='rating_categories',
            field=models.ManyToManyField(to='ratings.RatingCategory'),
        ),
    ]
