
from rest_framework import routers

from .views import AllProvidersViewSet, AddressViewSet, ContactViewSet, ProductViewSet, FactoryViewSet, \
    DilercenterViewSet, DistributorViewSet, RetailChainViewSet, IndividualEntrepreneurViewSet, SendEmailViewSet

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
router.register(r'send_email', SendEmailViewSet, basename='send_email')
urlpatterns = router.urls

