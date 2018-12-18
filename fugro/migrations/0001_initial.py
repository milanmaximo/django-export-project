# Generated by Django 2.1.4 on 2018-12-18 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fugro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('worktime', models.CharField(blank=True, max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('comment', models.TextField(blank='')),
                ('comment_project', models.TextField(blank='')),
                ('comment_equipment', models.TextField(blank='')),
                ('comment_car', models.TextField(blank='')),
                ('author', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='fugro.Author')),
                ('car', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='fugro.Car')),
            ],
            options={
                'verbose_name': 'fugro',
                'verbose_name_plural': 'fugros',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='fugro',
            name='project',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='fugro.Project'),
        ),
        migrations.AddField(
            model_name='fugro',
            name='utilisation',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='fugro.Utilisation'),
        ),
    ]
