# Generated by Django 2.0.2 on 2018-03-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20180323_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]