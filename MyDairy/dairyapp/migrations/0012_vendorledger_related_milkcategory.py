# Generated by Django 2.1.7 on 2019-03-05 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0011_auto_20190305_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorledger',
            name='related_milkcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendorledger', to='dairyapp.MilkCategory'),
        ),
    ]
