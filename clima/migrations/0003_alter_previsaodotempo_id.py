# Generated by Django 5.0.3 on 2024-03-16 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0002_alter_previsaodotempo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previsaodotempo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
