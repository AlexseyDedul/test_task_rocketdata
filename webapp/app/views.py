from decimal import Decimal

from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Address, Contact, Product, Factory, Dilercenter, IndividualEntrepreneur, RetailChain, Distributor, \
    Country
from .permissions import IsActiveUser, IsOwnerOrReadOnly
from .serializers import AddressSerializer, ContactSerializer, ProductSerializer, FactorySerializer, \
    DilercenterSerializer, EmployeeSerializer, IndividualEntrepreneurSerializer, RetailChainSerializer, \
    DistributorSerializer


class MyCustomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, IsActiveUser,)

    def create(self, request, *args, **kwargs):
        if isinstance(request.data['contact'], dict):
            serializer_contact = ContactSerializer(data=request.data['contact'])
            serializer_contact.is_valid(raise_exception=True)
            serializer_contact.save()
            request.data['contact'] = serializer_contact.data.get('id')
            request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({"Created"}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsActiveUser,)

    def create(self, request, **kwargs):
        validate = request.data
        serializer = AddressSerializer(data=validate)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({"created"}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsActiveUser,)

    def create(self, request, **kwargs):
        validate = request.data['contact']
        serializer = self.get_serializer(data=validate)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({"created"}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveUser,)


class FactoryViewSet(MyCustomViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class DilercenterViewSet(MyCustomViewSet):
    queryset = Dilercenter.objects.all()
    serializer_class = DilercenterSerializer


class DistributorViewSet(MyCustomViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer


class RetailChainViewSet(MyCustomViewSet):
    queryset = RetailChain.objects.all()
    serializer_class = RetailChainSerializer


class IndividualEntrepreneurViewSet(MyCustomViewSet):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class AllProvidersViewSet(viewsets.ViewSet):
    permission_classes = (IsActiveUser,)

    def list(self, request):
        factory = Factory.objects.all()
        dilercenter = Dilercenter.objects.all()
        distributor = Distributor.objects.all()
        rc = RetailChain.objects.all()
        ie = IndividualEntrepreneur.objects.all()

        return Response(self.__get_serialize_object(factory, dilercenter, distributor, rc, ie))

    @action(methods=['get'], detail=True, url_path='country_name')
    def search_by_country(self, request, pk=None):
        # try:
        country = get_object_or_404(Country, country_name=pk)
        if country:
            factory = Factory.objects.select_related('contact') \
                .filter(contact__address_fk__country=country.id)
            dilercenter = Dilercenter.objects.select_related('contact') \
                .filter(contact__address_fk__country=country.id)
            distributor = Distributor.objects.select_related('contact') \
                .filter(contact__address_fk__country=country.id)
            rc = RetailChain.objects.select_related('contact') \
                .filter(contact__address_fk__country=country.id)
            ie = IndividualEntrepreneur.objects.select_related('contact') \
                .filter(contact__address_fk__country=country.id)

            return Response(self.__get_serialize_object(factory, dilercenter, distributor, rc, ie))
        return Response({}, status.HTTP_404_NOT_FOUND)
        # except :
        #     print("ertyu")

    @action(methods=['get'], detail=True, url_path='product')
    def search_by_product_id(self, request, pk=None):
        if isinstance(pk, int):
            factory = get_object_or_404(Factory, product=pk)
            dilercenter = Dilercenter.objects.filter(product=pk)
            distributor = Distributor.objects.filter(product=pk)
            rc = RetailChain.objects.filter(product=pk)
            ie = IndividualEntrepreneur.objects.filter(product=pk)

            return Response(self.__get_serialize_object(factory, dilercenter, distributor, rc, ie))
        return Response({'detail': 'Страница не найдена.'}, status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True, url_path='big_debt')
    def search_by_big_debt(self, request, pk=None):
        avg = self.__get_avg_debt()
        factory = Factory.objects.exclude(debt__gt=avg)
        dilercenter = Dilercenter.objects.exclude(debt__gt=avg)
        distributor = Distributor.objects.exclude(debt__gt=avg)
        rc = RetailChain.objects.exclude(debt__gt=avg)
        ie = IndividualEntrepreneur.objects.exclude(debt__gt=avg)
        providers = self.__get_serialize_object(factory, dilercenter, distributor, rc, ie)
        providers['avg_providers'] = avg

        return Response(providers)

    def __get_avg_debt(self):
        list_providers = self.__get_list_providers()

        sum = Decimal()
        for item in list_providers:
            sum = sum + item.debt

        return sum / len(list_providers)

    def __get_list_providers(self):
        factory = Factory.objects.all()
        dilercenter = Dilercenter.objects.all()
        distributor = Distributor.objects.all()
        rc = RetailChain.objects.all()
        ie = IndividualEntrepreneur.objects.all()

        list_providers = [*factory, *dilercenter, *distributor, *rc, *ie]

        return list_providers

    def __get_serialize_object(self, factory, dilercenter, distributor, rc, ie):
        serializer_factory = FactorySerializer(factory, many=True)
        serializer_dilercenter = DilercenterSerializer(dilercenter, many=True)
        serializer_distributor = DistributorSerializer(distributor, many=True)
        serializer_rc = RetailChainSerializer(rc, many=True)
        serializer_ie = IndividualEntrepreneurSerializer(ie, many=True)
        return {
            "factory": serializer_factory.data,
            "dilercenter": serializer_dilercenter.data,
            "distributor": serializer_distributor.data,
            "retail_chain": serializer_rc.data,
            "individual_entrepreneur": serializer_ie.data
        }
