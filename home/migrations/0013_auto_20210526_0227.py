# Generated by Django 2.2.20 on 2021-05-26 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_merge_20210526_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_isreserved',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]