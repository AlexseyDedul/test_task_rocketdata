# Generated by Django 4.1.3 on 2022-11-07 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_dilercenter_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dilercenter',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='factory_field', to='app.factory'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dilercenter_field', to='app.dilercenter'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='retail_chain_field', to='app.retailchain'),
        ),
        migrations.AlterField(
            model_name='retailchain',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distributor_field', to='app.distributor'),
        ),
    ]
