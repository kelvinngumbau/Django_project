# Generated by Django 5.0.2 on 2024-03-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='chosen_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]
