# Generated by Django 3.0.3 on 2020-09-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_auto_20200909_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='content',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.TextField(default='（评论者）'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateField(default='1000-01-01'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='actor',
            name='introduction',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.TextField(default='（演员）'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='occupation',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coactor',
            name='coactor_name',
            field=models.TextField(default='（合作演员）'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default='1000-01-01'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(default='1000-01-01'),
        ),
    ]
