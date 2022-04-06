from core.models import Tag, Ingredient, Recipe
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Ingredient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""
    ingredients = serializers.PrimaryKeyRelatedField(many=True,
                                                     queryset=Ingredient.objects.all())

    tags = serializers.PrimaryKeyRelatedField(many=True,
                                              queryset=Tag.objects.all())

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ingredients', 'tags', 'time_minutes', 'price', 'link')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)


class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""

    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
