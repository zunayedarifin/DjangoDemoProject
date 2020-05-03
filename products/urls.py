from django.urls import path

from products import views

urlpatterns =[
    path('', views.product),
    path('new-product', views.newProduct)
]