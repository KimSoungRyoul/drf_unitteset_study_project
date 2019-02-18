# Generated by Django 2.1.7 on 2019-02-16 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('order', '0002_auto_20190216_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(help_text='주문을 소유한 회원', on_delete=django.db.models.deletion.CASCADE,
                                    to='account.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(help_text='주문된 상품들의 총 가격'),
        ),
    ]
