# Generated by Django 4.1.6 on 2023-02-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0014_alter_post_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]
