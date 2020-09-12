# Generated by Django 3.0.3 on 2020-09-07 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('director', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(through='movies.MovieActor', to='movies.Actor'),
        ),
    ]