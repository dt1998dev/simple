from rest_framework import serializers
from .models import Tag,TagBookLink,Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'

class TagBookLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=TagBookLink
        fields='__all__'


