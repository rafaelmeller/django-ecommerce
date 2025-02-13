from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to="products/", verbose_name="Product Image", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.name


class ProductVariation(models.Model):
    VARIATION_CHOICES = [
        ("size", "Size"),
        ("color", "Color"),
        ("model", "Model"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variations")
    variation_type = models.CharField(max_length=10, choices=VARIATION_CHOICES, verbose_name="Variation Type")
    value = models.CharField(max_length=50, verbose_name="Variation Value")
    stock = models.PositiveIntegerField(verbose_name="Variation Stock")  # Agora o estoque é específico para a variação

    def __str__(self):
        return f"{self.product.name} - {self.get_variation_type_display()}: {self.value}"

    class Meta:
        unique_together = ('product', 'variation_type', 'value')  # Garantir que cada combinação de variação seja única

