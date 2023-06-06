# Generated by Django 4.2.2 on 2023-06-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planApp1', '0005_schlagwort_alter_lernfeld_options_lernbaustein'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lernbaustein',
            options={'ordering': ['lernfeld__name', 'nummer'], 'verbose_name': 'Lernbaustein', 'verbose_name_plural': 'Lernbausteine'},
        ),
        migrations.AddField(
            model_name='lernbaustein',
            name='stunden',
            field=models.IntegerField(default=0, verbose_name='Sunden'),
        ),
    ]
