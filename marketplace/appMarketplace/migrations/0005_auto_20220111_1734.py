# Generated by Django 3.2.8 on 2022-01-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMarketplace', '0004_valoracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='valoracion',
            name='estrellas',
            field=models.IntegerField(),
        ),
    ]
