from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from pizza.models import Pizza
from .serializers import PizzaListSerializer
from django.shortcuts import get_object_or_404


class PizzaListView(GenericAPIView):
    serializer_class = PizzaListSerializer

    def get(self, request):
        pizza_type = request.GET.get('type', '')
        pizza_size = request.GET.get('size', '')
        if pizza_type == '' and pizza_size == '':
            self.queryset = Pizza.objects.all()
        elif not (pizza_type == '' and pizza_size == ''):
            self.queryset = Pizza.objects.filter(pizza_type=pizza_type, pizza_size=pizza_size)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PizzaCreateView(GenericAPIView):
    serializer_class = PizzaListSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PizzaEditView(GenericAPIView):
    serializer_class = PizzaListSerializer

    def put(self, request, pizza_id):
        pizza_data = get_object_or_404(Pizza, pk=pizza_id)
        serializer = self.serializer_class(pizza_data, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pizza_id):
        pizza_data = get_object_or_404(Pizza, pk=pizza_id)
        pizza_data.delete()
        return Response({"message": "Pizza deleted successfully"}, status=status.HTTP_200_OK)
