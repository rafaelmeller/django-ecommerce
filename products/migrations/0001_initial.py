# Generated by Django 5.1.5 on 2025-01-31 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Product Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_type', models.CharField(choices=[('size', 'Size'), ('color', 'Color'), ('model', 'Model')], max_length=10, verbose_name='Variation Type')),
                ('value', models.CharField(max_length=50, verbose_name='Variation Value')),
                ('stock', models.PositiveIntegerField(verbose_name='Variation Stock')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='products.product')),
            ],
            options={
                'unique_together': {('product', 'variation_type', 'value')},
            },
        ),
    ]
