from rest_framework import viewsets, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductPagination(pagination.PageNumberPagination):
    page_size = 10  # Default 10 items per page
    page_size_query_param = 'page_size'
    max_page_size = 50

class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Product CRUD, filtering, searching, and pagination."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination  # Enables pagination

    # Enable searching, filtering, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering
    filterset_fields = ['price', 'variations__value']  # Allows filtering by price & variation value

    # Searching
    search_fields = ['name', 'description']  # Allows searching by product name & description

    # Ordering
    ordering_fields = ['price', 'created_at']  # Allows sorting by price & date

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user when creating a product