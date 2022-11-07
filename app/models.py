from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    country_name = models.CharField(verbose_name="Страна", max_length=20)

    def __str__(self):
        return self.country_name


class Address(models.Model):
    country = models.ForeignKey(Country, verbose_name="Страна", related_name="country", on_delete=models.CASCADE)
    city = models.CharField(verbose_name="Город", max_length=20)
    street = models.CharField(verbose_name="Улица", max_length=20)
    number = models.IntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.number}"


class Contact(models.Model):
    email = models.EmailField(verbose_name="Email", max_length=254)
    address_fk = models.ForeignKey(Address, verbose_name="Адрес", related_name="address", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email} {self.address_fk}"


class Product(models.Model):
    title = models.CharField(verbose_name="Название продукта", max_length=254)
    model = models.CharField(verbose_name="Модель", max_length=30)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} {self.model}"


class Employee(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=254)

    def __str__(self):
        return f"Employee Factory {self.name}"


class Factory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=254)
    contact = models.ForeignKey(Contact, verbose_name="Контакт",
                                related_name="contact", on_delete=models.SET_NULL, null=True)
    employee = models.ManyToManyField(Employee)
    product = models.ManyToManyField(Product)
    debt = models.DecimalField(verbose_name="Долг перед поставщиком", decimal_places=2, max_digits=12)
    date_created = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dilercenter(models.Model):
    name = models.CharField(verbose_name="Название", max_length=254)
    contact = models.ForeignKey(Contact, verbose_name="Контакт",
                                related_name="contact_dilercenter", on_delete=models.SET_NULL, null=True)
    provider = models.ForeignKey(Factory, verbose_name="Поставщик",
                                 related_name="factory_field", on_delete=models.SET_NULL, null=True)
    employee = models.ManyToManyField(Employee)
    product = models.ManyToManyField(Product)
    debt = models.DecimalField(verbose_name="Задолжность перед поставщиком", decimal_places=2, max_digits=12)
    date_created = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return f"Dilercenter {self.name}"


class Distributor(models.Model):
    name = models.CharField(verbose_name="Название", max_length=254)
    contact = models.ForeignKey(Contact, verbose_name="Контакт",
                                related_name="contact_distributor", on_delete=models.SET_NULL, null=True)
    provider = models.ForeignKey(Dilercenter, verbose_name="Поставщик",
                                 related_name="dilercenter_field", on_delete=models.SET_NULL, null=True)
    employee = models.ManyToManyField(Employee)
    product = models.ManyToManyField(Product)
    debt = models.DecimalField(verbose_name="Задолжность перед поставщиком", decimal_places=2, max_digits=12)
    date_created = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return f"Distributor {self.name}"


class RetailChain(models.Model):
    name = models.CharField(verbose_name="Название", max_length=254)
    contact = models.ForeignKey(Contact, verbose_name="Контакт",
                                related_name="contact_retail_chain", on_delete=models.SET_NULL, null=True)
    provider = models.ForeignKey(Distributor, verbose_name="Поставщик",
                                 related_name="distributor_field", on_delete=models.SET_NULL, null=True)
    employee = models.ManyToManyField(Employee)
    product = models.ManyToManyField(Product)
    debt = models.DecimalField(verbose_name="Задолжность перед поставщиком", decimal_places=2, max_digits=12)
    date_created = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return f"Retail Chain {self.name}"


class IndividualEntrepreneur(models.Model):
    name = models.CharField(verbose_name="Название", max_length=254)
    contact = models.ForeignKey(Contact, verbose_name="Контакт",
                                related_name="contact_individual_entrepreneur", on_delete=models.SET_NULL, null=True)
    provider = models.ForeignKey(RetailChain, verbose_name="Поставщик",
                                 related_name="retail_chain_field", on_delete=models.SET_NULL, null=True)
    employee = models.ManyToManyField(Employee)
    product = models.ManyToManyField(Product)
    debt = models.DecimalField(verbose_name="Задолжность перед поставщиком", decimal_places=2, max_digits=12)
    date_created = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return f"Individual Entrepreneur {self.name}"

