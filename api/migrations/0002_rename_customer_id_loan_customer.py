# Generated by Django 4.0.3 on 2023-04-03 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
