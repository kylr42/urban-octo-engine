from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    @staticmethod
    def validate_name(value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Наименование товара должно содержать не менее 3 символов"
            )
        return value

    @staticmethod
    def validate_price(value):
        if value <= 0:
            raise serializers.ValidationError(
                "Цена товара должна быть больше 0"
            )
        return value

    @staticmethod
    def validate_description(value):
        if not value:
            return value

        for banned_word in ('запрещенное слово', 'другое запрещенное слово'):
            if banned_word in value:
                raise serializers.ValidationError(
                    f"Описание товара содержит запрещенное слово '{banned_word}'"
                )
        return value
