# Generated by Django 4.1.3 on 2022-11-04 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_distributor_alter_dilercenter_debt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productindistributor',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distributor', to='app.distributor'),
        ),
        migrations.CreateModel(
            name='RetailChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('debt', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_retail_chain', to='app.contact')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='distributor_field', to='app.distributor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInRetailChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_retail_chain', to='app.product')),
                ('retail_chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retail_chain', to='app.retailchain')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRetailChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('retail_chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.retailchain')),
            ],
        ),
    ]