from rest_framework.test import APIClient

from main.tests.base import APIBaseTestCase
from products.models import Product


class ProductTests(APIBaseTestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.product = Product.objects.create(name="Test product", price=100.00)

    def test_create_product(self):
        response = self.client.post("/api/v1/products/", {"name": "New product", "price": 200.00})
        product = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(product["name"], "New product")
        self.assertEqual(product["price"], "200.00")

    def test_list_products(self):
        response = self.client.get("/api/v1/products/")

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 1)
        self.assertIn("results", response.data)
        self.assertIsInstance(response.data["results"], list)

    def test_invalid_product_creation(self):
        response = self.client.post("/api/v1/products/", {"name": "New product"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Product.objects.count(), 1)
        self.assertIn("price", response.data)
        self.assertEqual(response.json()["price"][0], "Обязательное поле.")
