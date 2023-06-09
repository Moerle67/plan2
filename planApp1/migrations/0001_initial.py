# Generated by Django 4.2.2 on 2023-06-06 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abteilung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Abteilung')),
                ('beschreibung', models.TextField(verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Abteilung',
                'verbose_name_plural': 'Abteilungen',
            },
        ),
        migrations.CreateModel(
            name='Lernfeld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2, verbose_name='Lernfeld Nr:')),
                ('inhalt', models.CharField(max_length=100, verbose_name='Inhalt')),
                ('beschreibung', models.TextField(verbose_name='Beschreibung')),
                ('stunden_jahr1', models.IntegerField(verbose_name='Anzahl der Stunden (1.Jahr)')),
                ('stunden_jahr2', models.IntegerField(verbose_name='Anzahl der Stunden (2.Jahr)')),
                ('stunden_jahr3', models.IntegerField(verbose_name='Anzahl der Stunden (3.Jahr)')),
            ],
            options={
                'verbose_name': 'Lernfeld',
                'verbose_name_plural': 'Lernfelder',
            },
        ),
        migrations.CreateModel(
            name='Ausbilungsberuf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Beruf')),
                ('details', models.CharField(max_length=50, verbose_name='detailiert Beruf')),
                ('beschreibung', models.TextField(verbose_name='Beschreibung')),
                ('abteilung', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='planApp1.abteilung', verbose_name='Abteilung')),
            ],
            options={
                'verbose_name': 'Ausbilungsberuf',
                'verbose_name_plural': 'Ausbilungsberufe',
            },
        ),
    ]
