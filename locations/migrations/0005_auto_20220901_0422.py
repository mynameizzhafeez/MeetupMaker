# Generated by Django 3.1 on 2022-09-01 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20220901_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halal',
            name='mall',
            field=models.ForeignKey(db_column='mall', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='halal_stores', to='locations.mall'),
        ),
        migrations.AlterField(
            model_name='mall',
            name='mrt',
            field=models.ForeignKey(db_column='mrt', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='malls', to='locations.mrt'),
        ),
    ]
