# Generated by Django 3.1.7 on 2021-07-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210713_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='watchlist1',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.movies'),
        ),
    ]
