# Generated by Django 4.0.3 on 2022-04-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
    ]
