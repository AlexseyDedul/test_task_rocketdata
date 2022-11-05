from rest_framework import serializers
from .models import Address, Contact, Product, Factory, Dilercenter, Employee
from django.db import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "title", "model"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    product = ProductSerializer(many=True)
    employee = EmployeeSerializer(many=True)

    class Meta:
        model = Factory
        # fields = "__all__"
        fields = ["id", "name", "contact", "product", "employee"]
        read_only_fields = ['debt']


class DilercenterSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    product = ProductSerializer(many=True)
    employee = EmployeeSerializer(many=True)

    class Meta:
        model = Dilercenter
        # fields = "__all__"
        fields = ["id", "name", "contact", "product", "employee", "debt"]