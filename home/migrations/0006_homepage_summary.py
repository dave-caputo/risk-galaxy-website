# Generated by Django 2.0.2 on 2018-03-30 16:22

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_login_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='summary',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
