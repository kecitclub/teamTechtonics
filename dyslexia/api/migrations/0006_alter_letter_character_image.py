# Generated by Django 5.1.4 on 2025-01-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_letter_character_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='character_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='character_images/'),
        ),
    ]
