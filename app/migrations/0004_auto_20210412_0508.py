# Generated by Django 3.1.7 on 2021-04-12 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_travel_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='SEAT',
            field=models.CharField(choices=[('GENERAL', 'GENERAL'), ('LADIES', 'LADIES'), ('LOWER BERTH/SR. CITIZEN', 'LOWER BERTH/SR. CITIZEN'), ('DIVYANG', 'DIVYANG')], default='GENERAL', max_length=50),
        ),
        migrations.AlterField(
            model_name='travel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
