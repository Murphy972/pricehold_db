# Generated by Django 2.2.20 on 2021-04-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210427_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_ismarked',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_isreserved',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]