# Generated by Django 5.1.1 on 2024-10-17 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newslettersubscriber',
            name='last_sent',
        ),
        migrations.RemoveField(
            model_name='newslettersubscriber',
            name='name',
        ),
    ]
