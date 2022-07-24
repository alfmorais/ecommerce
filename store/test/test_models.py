from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data = Category.objects.create(
            name="Django",
            slug="django",
        )

    def test_category_model_entry(self):
        """
        Test Category Model data insertion/types/field attributes.
        """
        condition = isinstance(self.data, Category)
        self.assertTrue(condition)

    def test_category_return_name(self):
        """
        Test Category Model returning name in def __str__.
        """
        self.assertEqual(self.data.__str__(), "Django")


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name="Django", slug="django")
        User.objects.create(username="admin")

        self.data = Product.objects.create(
            category_id=1,
            title="django beginners",
            created_by_id=1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )

    def test_product_model_entry(self):
        """
        Test Product Model data insertion/types/field attributes.
        """
        condition = isinstance(self.data, Product)
        self.assertTrue(condition)

    def test_product_return_title(self):
        """
        Test Product Model returning title in def __str__.
        """
        self.assertEqual(self.data.__str__(), "django beginners")
