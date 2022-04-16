from django.urls import path, include
from rest_framework import routers

from main.views import AnnouncementViewSet, CategoryViewSet, SubcategoryViewSet

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementViewSet,
                basename='announcements')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'subcategories', SubcategoryViewSet, basename='subcategories')

urlpatterns = [
    path('main/', include(router.urls))
]
