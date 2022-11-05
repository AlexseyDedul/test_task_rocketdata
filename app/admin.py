from django.contrib import admin
from django.db.models.query import Prefetch
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.http import urlencode

# Register your models here.

from .models import Address, Contact, Country, \
    Factory, Product, Dilercenter, \
    Distributor, RetailChain, IndividualEntrepreneur, Employee


@admin.action(description='Обнулить задолжность перед поставщиком')
def make_published(modeladmin, request, queryset):
    temp = queryset.exclude(debt__gt=0)
    temp.update(debt=0)


class MyAdmin(admin.ModelAdmin):
    def get_search_results(self, request, queryset, search_term):
        use_distinct = False

        if search_term:
            search_result = queryset \
                .select_related('contact') \
                .filter(contact__address_fk__city__contains=search_term)
            return search_result, use_distinct
        return queryset, use_distinct


class FactoryAdmin(MyAdmin):
    list_display = ('id', 'name', 'contact', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('get_search_results',)
    actions = [make_published]


class DilercenterAdmin(MyAdmin):
    list_display = ('id', 'name', 'contact', 'show_provider', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('get_search_results',)
    actions = [make_published]

    def show_provider(self, obj):
        provider = Factory.objects.filter(id=obj.provider.id).first()
        return mark_safe(f'<a href="/admin/app/factory/{provider.id}/change/">{obj.provider}</a>')


class DistributorAdmin(MyAdmin):
    list_display = ('id', 'name', 'contact', 'show_provider', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('get_search_results',)
    actions = [make_published]

    def show_provider(self, obj):
        provider = Dilercenter.objects.filter(id=obj.provider.id).first()
        return mark_safe(f'<a href="/admin/app/dilercenter/{provider.id}/change/">{obj.provider}</a>')


class RetailChainAdmin(MyAdmin):
    list_display = ('id', 'name', 'contact', 'show_provider', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('get_search_results',)
    actions = [make_published]

    def show_provider(self, obj):
        provider = Distributor.objects.filter(id=obj.provider.id).first()
        return mark_safe(f'<a href="/admin/app/distributor/{provider.id}/change/">{obj.provider}</a>')


class IndividualEntrepreneurAdmin(MyAdmin):
    list_display = ('id', 'name', 'contact', 'show_provider', 'debt', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('get_search_results',)
    actions = [make_published]

    def show_provider(self, obj):
        provider = RetailChain.objects.filter(id=obj.provider.id).first()
        return mark_safe(f'<a href="/admin/app/retailchain/{provider.id}/change/">{obj.provider}</a>')


admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Dilercenter, DilercenterAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(RetailChain, RetailChainAdmin)
admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)
