from django.contrib import admin

from product.models import ProductCategory, Product, Basket, FilterBrand, FilterCountry, FilterMaterial

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(FilterBrand)
admin.site.register(FilterCountry)
admin.site.register(FilterMaterial)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'shor_description', ('price', 'quantity'), 'category')
    # readonly_fields = ('shor_description',)
    search_fields = ('name',)


# @admin.register(Subscribe)
# class SubscribeAdmin(admin.ModelAdmin):
#     list_display = ('email1', 'date')
#     readonly_fields = ('email1', 'date')
#     # search_fields = ('data',)


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('catalog', 'quantity',)
    # readonly_fields = ('created',)


class FilterCategoryAdmin(admin.ModelAdmin):
    model = FilterBrand, FilterCountry, FilterMaterial
    fields = ('brand', 'material', 'country')







