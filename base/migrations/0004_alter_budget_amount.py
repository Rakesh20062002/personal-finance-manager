# Generated by Django 5.0.4 on 2024-12-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_budget_created_at_budget_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
