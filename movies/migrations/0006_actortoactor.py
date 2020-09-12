# Generated by Django 3.0.3 on 2020-09-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20200908_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorToActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor1', models.ForeignKey(blank=True, db_column='actor1', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='actor1', to='movies.Actor')),
                ('actor2', models.ForeignKey(blank=True, db_column='actor2', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.Actor')),
            ],
        ),
    ]
