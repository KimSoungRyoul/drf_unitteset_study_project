# Generated by Django 2.1.7 on 2019-02-16 10:25

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('account', '0002_auto_20190216_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('total_price', models.PositiveIntegerField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Customer')),
            ],
        ),
    ]
