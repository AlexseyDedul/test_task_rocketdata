from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=20)

    def __str__(self):
        return self.country_name


class Address(models.Model):
    country = models.ForeignKey(Country, related_name="country", on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    number = models.IntegerField()

    def __str__(self):
        address_full = f"{self.country} {self.city} {self.street} {self.number}"
        return address_full


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    address_fk = models.ForeignKey(Address, related_name="address", on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Product(models.Model):
    title = models.CharField(max_length=254)
    model = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} {self.model}"


class Factory(models.Model):
    name = models.CharField(max_length=254)
    contact = models.ForeignKey(Contact, related_name="contact", on_delete=models.CASCADE)
    debt = models.DecimalField(decimal_places=2, max_digits=12)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductInFactory(models.Model):
    factory = models.ForeignKey(Factory, related_name="factory", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)


class EmployeeFactory(models.Model):
    name = models.CharField(max_length=254)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee Factory {self.name}"


class Dilercenter(models.Model):
    name = models.CharField(max_length=254)
    contact = models.ForeignKey(Contact, related_name="contact_dilercenter", on_delete=models.CASCADE)
    provider = models.ForeignKey(Factory, related_name="factory_field", on_delete=models.PROTECT)
    debt = models.DecimalField(decimal_places=2, max_digits=12)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Dilercenter {self.name}"


class ProductInDilercenter(models.Model):
    dilercenter = models.ForeignKey(Dilercenter, related_name="dilercenter", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_dilercenter", on_delete=models.CASCADE)


class EmployeeDilercenter(models.Model):
    name = models.CharField(max_length=254)
    dilercenter = models.ForeignKey(Dilercenter, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee Dilercenter {self.name}"


class Distributor(models.Model):
    name = models.CharField(max_length=254)
    contact = models.ForeignKey(Contact, related_name="contact_distributor", on_delete=models.CASCADE)
    provider = models.ForeignKey(Dilercenter, related_name="dilercenter_field", on_delete=models.PROTECT)
    debt = models.DecimalField(decimal_places=2, max_digits=12)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Distributor {self.name}"


class ProductInDistributor(models.Model):
    distributor = models.ForeignKey(Distributor, related_name="distributor", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_distributor", on_delete=models.CASCADE)


class EmployeeDistributor(models.Model):
    name = models.CharField(max_length=254)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee Distributor {self.name}"


class RetailChain(models.Model):
    name = models.CharField(max_length=254)
    contact = models.ForeignKey(Contact, related_name="contact_retail_chain", on_delete=models.CASCADE)
    provider = models.ForeignKey(Distributor, related_name="distributor_field", on_delete=models.PROTECT)
    debt = models.DecimalField(decimal_places=2, max_digits=12)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Retail Chain {self.name}"


class ProductInRetailChain(models.Model):
    retail_chain = models.ForeignKey(RetailChain, related_name="retail_chain", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_retail_chain", on_delete=models.CASCADE)


class EmployeeRetailChain(models.Model):
    name = models.CharField(max_length=254)
    retail_chain = models.ForeignKey(RetailChain, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee Retail Chain {self.name}"


class IndividualEntrepreneur(models.Model):
    name = models.CharField(max_length=254)
    contact = models.ForeignKey(Contact, related_name="contact_individual_entrepreneur", on_delete=models.CASCADE)
    provider = models.ForeignKey(RetailChain, related_name="retail_chain_field", on_delete=models.PROTECT)
    debt = models.DecimalField(decimal_places=2, max_digits=12)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Individual Entrepreneur {self.name}"


class ProductInIndividualEntrepreneur(models.Model):
    individual_entrepreneur = models.ForeignKey(IndividualEntrepreneur, related_name="individual_entrepreneur", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_individual_entrepreneur", on_delete=models.CASCADE)


class EmployeeIndividualEntrepreneur(models.Model):
    name = models.CharField(max_length=254)
    individual_entrepreneur = models.ForeignKey(IndividualEntrepreneur, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee Individual Entrepreneur {self.name}"
