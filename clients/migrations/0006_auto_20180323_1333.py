# Generated by Django 2.0.2 on 2018-03-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20180323_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('-modified',)},
        ),
    ]
