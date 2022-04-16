from rest_framework import serializers
from main.models import Announcement, Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('id', 'title', 'category')


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'subcategory')


class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'description', 'image', 'user', 'category', 'subcategory',
                  'price', 'address', 'created', 'updated')
