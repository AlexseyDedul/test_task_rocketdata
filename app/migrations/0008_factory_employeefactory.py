# Generated by Django 4.1.3 on 2022-11-04 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('debt', models.DecimalField(decimal_places=2, max_digits=2)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='app.contact')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeFactory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.factory')),
            ],
        ),
    ]
