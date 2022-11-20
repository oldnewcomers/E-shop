from django.urls import path , include
from base.views import GetRoutes , GetProduct , GetProducts

urlpatterns = [
    path("" , GetRoutes , name = "Routes"),
    path("products/" , GetProducts.as_view() , name = "Products"),
    path("product/<str:pk>/", GetProduct.as_view() , name = "Product"),
]

