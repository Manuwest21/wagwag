# Generated by Django 4.1.2 on 2022-10-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='text',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
