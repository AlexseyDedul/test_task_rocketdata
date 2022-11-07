from collections import OrderedDict
import datetime

from rest_framework import serializers
from .models import Address, Contact, Product, Factory, Dilercenter, Employee, IndividualEntrepreneur, RetailChain, \
    Distributor


class MyCustomSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        dilercenter_create = self.Meta.model.objects.create(
            name=validated_data['name'],
            contact=validated_data['contact'],
            provider=validated_data['provider'],
            debt=0.0,
            user=validated_data['user']
        )
        for prod in validated_data['product']:
            product = Product.objects.get(id=prod.id)
            dilercenter_create.product.add(product)

        for empl in validated_data['employee']:
            employee = Employee.objects.get(id=empl.id)
            dilercenter_create.employee.add(employee)
        return dilercenter_create


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def create(self, validated_data):
        return Address.objects.create(**validated_data)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def validate(self, attrs):
        if len(attrs['title']) > 25:
            raise serializers.ValidationError({"title": "Название продукта должно быть меньше 25 символов"})
        print(attrs['date'])
        if attrs['date'] > datetime.date.today():
            raise serializers.ValidationError(
                {"date": "Дата выпуска продукта на выход не может быть больше сегоднешнего дня."})

        return attrs


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Factory
        fields = "__all__"
        read_only_fields = ['debt']

    def create(self, validated_data):
        factory_create = Factory.objects.create(
            name=validated_data['name'],
            contact=validated_data['contact'],
            debt=0.0,
            user=validated_data['user']
        )
        for prod in validated_data['product']:
            product = Product.objects.get(id=prod.id)
            factory_create.product.add(product)

        for empl in validated_data['employee']:
            employee = Employee.objects.get(id=empl.id)
            factory_create.employee.add(employee)
        return factory_create

    def validate(self, attrs):
        if len(attrs['name']) > 50:
            raise serializers.ValidationError({"name": "Название должно быть меньше 50 символов"})

        return attrs


class DilercenterSerializer(MyCustomSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Dilercenter
        fields = "__all__"
        read_only_fields = ['debt']


class DistributorSerializer(MyCustomSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Distributor
        fields = "__all__"
        read_only_fields = ['debt']


class RetailChainSerializer(MyCustomSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RetailChain
        fields = "__all__"
        read_only_fields = ['debt']


class IndividualEntrepreneurSerializer(MyCustomSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = IndividualEntrepreneur
        fields = "__all__"
        read_only_fields = ['debt']
