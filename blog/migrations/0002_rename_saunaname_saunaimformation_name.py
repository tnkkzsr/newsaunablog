# Generated by Django 3.2.6 on 2022-10-26 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saunaimformation',
            old_name='Saunaname',
            new_name='name',
        ),
    ]
