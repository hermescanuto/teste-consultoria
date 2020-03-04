from rest_framework import serializers

from demand.models import Demand, Category, People
from upload.models import Document


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['identificator', 'name', 'phone', 'gender']


class DemandSerializer(serializers.ModelSerializer):
    people = PeopleSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Demand
        fields = ['id', 'people', 'category', 'demand', 'date']
