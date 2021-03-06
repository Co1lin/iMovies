# Generated by Django 3.0.3 on 2020-09-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_introduction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='nationality',
        ),
        migrations.AddField(
            model_name='actor',
            name='birthday',
            field=models.DateField(default='2020-09-08', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actor',
            name='gender',
            field=models.CharField(default='男', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actor',
            name='introduction',
            field=models.CharField(default='全是演员。', max_length=700),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actor',
            name='occupation',
            field=models.CharField(default='演员/导演', max_length=30),
            preserve_default=False,
        ),
    ]
