# Generated by Django 4.2.2 on 2023-06-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planApp1', '0003_rename_ausbilungsberuf_ausbildungsberuf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lernfeld',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Lernfeld Nr:'),
        ),
    ]
