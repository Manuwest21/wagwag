# Generated by Django 4.1.2 on 2022-10-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flexpage',
            options={'verbose_name': 'Page divers', 'verbose_name_plural': 'Pages divers'},
        ),
        migrations.AlterField(
            model_name='flexpage',
            name='text',
            field=models.TextField(blank=True, default='Non non dolor non dolorem dolor. Neque amet dolor est sit tempora tempora sit. Neque etincidunt consectetur labore porro amet porro. Dolor sed consectetur ipsum modi voluptatem voluptatem. Non magnam consectetur non amet modi eius. Labore dolore quiquia dolorem quiquia. Labore consectetur dolorem non magnam non magnam magnam. Dolorem eius ipsum numquam.', max_length=600, null=True),
        ),
    ]
