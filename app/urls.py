from django.urls import path

from app.views import AddressViewSet, ContactViewSet, ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet, basename='address')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'product', ProductViewSet, basename='product')
urlpatterns = router.urls

# urlpatterns = [
#     path('address/', AddressViewSet.as_view({'get': 'list'})),
#     path('address/<int:pk>', AddressViewSet.as_view({'get': 'retrieve'})),
#     path('contact/', ContactViewSet.as_view({'get': 'list'})),
# ]
