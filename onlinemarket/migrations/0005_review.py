# Generated by Django 4.2 on 2023-05-22 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('onlinemarket', '0004_order_orderproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=300)),
                ('rate', models.PositiveBigIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Bad'), (3, '3 - Ok'), (4, '4 - Good'), (5, '5 - Perfect')], null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinemarket.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
