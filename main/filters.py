from main.models import Announcement
from django_filters import rest_framework as filters

class AnnouncementFilter(filters.FilterSet):

    class Meta:
        model = Announcement
        fields = ('category', 'subcategory')
