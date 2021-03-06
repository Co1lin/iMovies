# Generated by Django 3.0.3 on 2020-09-08 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_coactorid_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coactor_id', models.IntegerField()),
                ('coactor_name', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Actor')),
            ],
        ),
        migrations.DeleteModel(
            name='CoActorID',
        ),
    ]
