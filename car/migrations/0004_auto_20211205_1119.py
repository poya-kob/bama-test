# Generated by Django 3.2.9 on 2021-12-05 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_auto_20211205_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carprice',
            name='Amount_per_payment',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='carprice',
            name='delivery_time',
            field=models.IntegerField(choices=[(1, '1 day'), (7, '7 day'), (12, '12 day'), (20, '20 day'), (30, '30 day'), (45, '45 day')], null=True),
        ),
        migrations.AlterField(
            model_name='carprice',
            name='number_of_payments',
            field=models.CharField(choices=[(1, '1 pays'), (2, '2 pays'), (3, '3 pays'), (4, '4 pays'), (5, '5 pays'), (6, '6 pays'), (7, '7 pays'), (8, '8 pays'), (9, '9 pays'), (10, '10 pays')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carprice',
            name='payment_period',
            field=models.IntegerField(choices=[(0, 'every month '), (2, 'every 2 month '), (3, 'every 3 month '), (4, 'every 4 month ')], null=True),
        ),
        migrations.AlterField(
            model_name='carprice',
            name='prepayment',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='carprice',
            name='price',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='carprice',
            name='second_prepayment',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
