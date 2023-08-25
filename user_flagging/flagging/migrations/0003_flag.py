# Generated by Django 4.2.4 on 2023-08-25 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagging', '0002_customer_delete_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Message', models.CharField(blank=True, max_length=200)),
                ('Customer', models.ManyToManyField(related_name='flags', to='flagging.customer')),
            ],
        ),
    ]