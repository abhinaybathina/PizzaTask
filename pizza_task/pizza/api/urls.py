from django.urls import path
from .views import PizzaListView, PizzaCreateView, PizzaEditView


urlpatterns = [
    path('list-pizza', PizzaListView.as_view(), name="pizza-list"),
    path('create-pizza', PizzaCreateView.as_view(), name="pizza-create"),
    path('edit-pizza/<int:pizza_id>', PizzaEditView.as_view(), name="pizza-edit"),
]
