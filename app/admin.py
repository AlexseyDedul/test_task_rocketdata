from django.contrib import admin
from django.db.models.query import Prefetch
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.http import urlencode

# Register your models here.

from .models import Address, Contact, Country, \
    Factory, EmployeeFactory, ProductInFactory, \
    Dilercenter, ProductInDilercenter, EmployeeDilercenter, \
    Distributor, ProductInDistributor, EmployeeDistributor, \
    RetailChain, ProductInRetailChain, EmployeeRetailChain, \
    IndividualEntrepreneur, ProductInIndividualEntrepreneur, EmployeeIndividualEntrepreneur


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def get_search_results(self, request, queryset, search_term):

        print(request)
        print(queryset)
        print(search_term)

        queryset = Factory.objects\
            .select_related('contact').all()\
            .select_related('address')\
            .filter(address_id=1)
        print(queryset)
        use_distinct = True
        # queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        # print(use_distinct)
        # print(queryset)
        # try:
        #     search_term_as_int = int(search_term)
        # except ValueError:
        #     pass
        # else:
        #     queryset |= self.model.objects.filter(age=search_term_as_int)
        return queryset , use_distinct


class DilercenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'show_provider', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('provider',)

    def show_provider(self, obj):
        provider = Factory.objects.filter(id=obj.provider.id).first()
        return mark_safe(f'<a href="/admin/app/factory/{provider.id}/change/">{obj.provider}</a>')


class DistributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'show_provider', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('provider',)

    def show_provider(self, obj):
        provider = Dilercenter.objects.filter(id=obj.provider.id).first()
        return mark_safe(f'<a href="/admin/app/dilercenter/{provider.id}/change/">{obj.provider}</a>')


class RetailChainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'show_provider', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('provider',)

    def show_provider(self, obj):
        provider = Distributor.objects.filter(id=obj.provider.id).first()
        return mark_safe(f'<a href="/admin/app/distributor/{provider.id}/change/">{obj.provider}</a>')


class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'show_provider', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('provider',)

    def show_provider(self, obj):
        provider = RetailChain.objects.filter(id=obj.provider.id).first()
        return mark_safe(f'<a href="/admin/app/retailchain/{provider.id}/change/">{obj.provider}</a>')


admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(EmployeeFactory)
admin.site.register(ProductInFactory)
admin.site.register(Dilercenter, DilercenterAdmin)
admin.site.register(ProductInDilercenter)
admin.site.register(EmployeeDilercenter)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(ProductInDistributor)
admin.site.register(EmployeeDistributor)
admin.site.register(RetailChain, RetailChainAdmin)
admin.site.register(ProductInRetailChain)
admin.site.register(EmployeeRetailChain)
admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)
admin.site.register(ProductInIndividualEntrepreneur)
admin.site.register(EmployeeIndividualEntrepreneur)
