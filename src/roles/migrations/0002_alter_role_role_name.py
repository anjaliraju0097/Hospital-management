# Generated by Django 4.0.3 on 2024-06-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]
