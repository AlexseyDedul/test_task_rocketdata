from rest_framework import viewsets

from .models import Address, Contact, Product, Factory, Dilercenter
from .serializers import AddressSerializer, ContactSerializer, ProductSerializer, FactorySerializer, \
    DilercenterSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class DilercenterViewSet(viewsets.ModelViewSet):
    queryset = Dilercenter.objects.all()
    serializer_class = DilercenterSerializer
