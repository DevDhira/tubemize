# Generated by Django 4.1.3 on 2022-11-30 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerpayment',
            old_name='subscription_id',
            new_name='subscriptionid',
        ),
    ]
