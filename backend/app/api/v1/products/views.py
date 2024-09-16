from django.db import transaction
from rest_framework import generics

from main.logger import get_logger
from products.models import Product
from products.metrics import products_created_total, total_product_price
from .serializers import ProductSerializer


logger = get_logger()


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        super().perform_create(serializer)

        products_created_total.inc()
        total_product_price.inc(float(serializer.instance.price))

        logger.info(
            "[ProductListCreateView] Product created successfully",
            extra={
                "product_id": serializer.instance.id,
                "product_name": serializer.instance.name,
                "product_price": serializer.instance.price,
            },
        )
