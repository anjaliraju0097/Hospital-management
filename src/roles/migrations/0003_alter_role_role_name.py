# Generated by Django 4.0.3 on 2024-06-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_alter_role_role_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
