# Generated by Django 3.2.6 on 2022-10-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_saunaimformation_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='saunaimformation',
            name='rouryu',
            field=models.BooleanField(default=False),
        ),
    ]
