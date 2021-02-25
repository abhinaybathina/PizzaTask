from rest_framework import serializers
from pizza.models import Pizza


class PizzaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

    def validate(self, attrs):
        pizza_type = attrs.get('pizza_type', '')
        pizza_size = attrs.get('pizza_size', '')
        if not (pizza_type == 'Regular' or pizza_type == 'Square'):
            raise serializers.ValidationError('Pizza type should be Regular or Square only!')
        if not (pizza_size == 'Small' or pizza_size == 'Medium' or pizza_size == 'Large' or pizza_size == 'Extra Large'):
            raise serializers.ValidationError('Pizza size should be Small/Medium/Large/Extra Large only!')
        return attrs

    def create(self, validated_data):
        return Pizza.objects.create(**validated_data)
