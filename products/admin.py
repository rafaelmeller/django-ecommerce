from django.contrib import admin
from .models import Product, ProductVariation

# Inline for ProductVariation to show variations within the Product admin page
class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1  # Number of empty forms displayed to add new variations
    fields = ('variation_type', 'value', 'stock')  # Display fields for each variation
    readonly_fields = ('stock',)  # If you want the stock to be readonly

# Admin for Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')  # Updated: No stock here
    search_fields = ('name',)
    inlines = [ProductVariationInline]  # Display variations inline within Product

# Admin for ProductVariation model
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_type', 'value', 'stock')  # Display product, variation type, value, and stock
    list_filter = ('variation_type',)
    search_fields = ('product__name',)  # Search variations by product name
    ordering = ('product',)

# Register models in the admin
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)

