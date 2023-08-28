# Generated by Django 4.2.4 on 2023-08-28 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagging', '0004_remove_customer_businesses_flag_businesses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flag',
            name='Customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='flags',
            field=models.ManyToManyField(to='flagging.flag'),
        ),
    ]
