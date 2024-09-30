from django.urls import path, include

from product.views import product, basket_add, basket_delete, search, product_details, privacy, checkout

app_name = 'product'

urlpatterns = [
    path('', product, name='index'),
    path('search/', search, name='search'),
    path('category/<int:category_id>/', product, name='category'),
    path('page/<int:page>/', product, name='page'),
    path('brand/<str:brand>/', product, name='brand'),
    path('country/<str:country>/', product, name='country'),
    path('material/<str:material>/', product, name='material'),
    path('sort/<str:sort>/', product, name='sort'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', basket_delete, name='basket_delete'),
    path('checkout/', checkout, name='checkout'),
    path('details/<int:prod_id>/', product_details, name='product_details'),

]
