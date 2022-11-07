from django.urls import path

from app.views import AddressViewSet, ContactViewSet, ProductViewSet, FactoryViewSet, DilercenterViewSet, \
    DistributorViewSet, RetailChainViewSet, IndividualEntrepreneurViewSet, AllProvidersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all', AllProvidersViewSet, basename='all')
router.register(r'all/search', AllProvidersViewSet, basename='search')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'factory', FactoryViewSet, basename='factory')
router.register(r'dilercenter', DilercenterViewSet, basename='dilercenter')
router.register(r'distributor', DistributorViewSet, basename='distributor')
router.register(r'retail_chain', RetailChainViewSet, basename='retail_chain')
router.register(r'individual_entrepreneur', IndividualEntrepreneurViewSet, basename='individual_entrepreneur')
urlpatterns = router.urls

# urlpatterns = [
#     path('address/', AddressViewSet.as_view({'get': 'list'})),
#     path('address/<int:pk>', AddressViewSet.as_view({'get': 'retrieve'})),
#     path('contact/', ContactViewSet.as_view({'get': 'list'})),
# ]
