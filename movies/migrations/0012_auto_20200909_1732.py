# Generated by Django 3.0.3 on 2020-09-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_actor_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='language',
        ),
        migrations.AddField(
            model_name='movie',
            name='region',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='movie',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(default='1970-01-01'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='introduction',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.TextField(default='（电影）'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='scriptwriter',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.TextField(default=''),
        ),
    ]
