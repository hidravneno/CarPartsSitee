# Generated by Django 5.2.1 on 2025-06-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_part_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='category',
            field=models.CharField(choices=[('Engine', 'Engine'), ('Brakes', 'Brakes'), ('Suspension', 'Suspension'), ('Electrical', 'Electrical'), ('Interior', 'Interior'), ('Body', 'Body'), ('Tires', 'Tires'), ('Motor oil', 'Motor oil')], max_length=50),
        ),
    ]
