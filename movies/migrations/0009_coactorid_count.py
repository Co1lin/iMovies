# Generated by Django 3.0.3 on 2020-09-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_coactorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='coactorid',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
