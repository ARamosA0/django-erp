# Generated by Django 3.2 on 2023-01-20 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_remision_clie_contador'),
    ]

    operations = [
        migrations.AddField(
            model_name='remision_clie',
            name='contador',
            field=models.IntegerField(default=0, null=True),
        ),
    ]