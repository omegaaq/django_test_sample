from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("show_clients/", views.show_clients, name="show_clients"),
    path("show_client/<int:id>/", views.show_client, name="show_client"),
    path("show_salesman/", views.show_salesman, name="show_salesman"),
    path("show_seller/<int:id>/", views.show_seller, name="show_seller"),
    path("show_products/", views.show_products, name="show_products"),
    path("show_sales/", views.show_sales, name="show_sales"),
    path("add_client/", views.add_client, name="add_client"),
    path("add_sale/", views.add_sale, name="add_sale"),
    path("delete_sale/", views.delete_sale, name="delete_sale"),
]
