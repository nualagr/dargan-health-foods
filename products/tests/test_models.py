from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from ..models import (
    Brand,
    Department,
    Category,
    Tag,
    Product,
    ProductImage,
    ProductTag,
    ProductReview,
)
from cart.models import DiscountCode


class TestProductModels(TestCase):
    def setUp(self):
        """
        Create a DiscountCode, SuperUser, Brand,
        Department, Category, Tag and Product for
        testing purposes.
        """
        discount_code = DiscountCode.objects.create(
            discount_code="NEW10",
            percentage_discount=10
        )
        self.client = Client()
        self.user = User.objects.create_superuser(
            "admin", "admin@darganhealthfoods.com", "adminpassword"
        )
        brand = Brand.objects.create(
            name="test_brand",
            friendly_name="Test Brand"
        )
        department = Department.objects.create(
            name="test_department",
            friendly_name="Test Department"
        )
        category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category",
            department=department
        )
        tag = Tag.objects.create(
            name="test_tag",
            friendly_name="Test Tag"
        )
        product = Product.objects.create(
            name="test_product",
            friendly_name="Test Product",
            price=0.00,
            brand=brand,
            category=category,
        )

    def test_brand_creation(self):
        """
        Test that Brands are created using the Brand
        model.
        """
        b = Brand.objects.get(name="test_brand")
        self.assertTrue(isinstance(b, Brand))

    def test_brand_string_method(self):
        """
        Test that Brands return the correct string.
        """
        b = Brand.objects.get(name="test_brand")
        self.assertEqual(str(b), "test_brand")

    def test_brand_get_friendly_name_method(self):
        """
        Test that Brands return the correct friendly name.
        """
        b = Brand.objects.get(name="test_brand")
        self.assertEqual(b.get_friendly_name(), "Test Brand")

    def test_department_creation(self):
        """
        Test that Departments are created using the Department
        model.
        """
        d = Department.objects.get(name="test_department")
        self.assertTrue(isinstance(d, Department))

    def test_department_string_method(self):
        """
        Test that Departments return the correct string.
        """
        d = Department.objects.get(name="test_department")
        self.assertEqual(str(d), "test_department")

    def test_department_get_friendly_name_method(self):
        """
        Test that Departments return the correct friendly name.
        """
        d = Department.objects.get(name="test_department")
        self.assertEqual(d.get_friendly_name(), "Test Department")

    def test_category_creation(self):
        """
        Test that Categories are created using the Category
        model.
        """
        c = Category.objects.get(name="test_category")
        self.assertTrue(isinstance(c, Category))

    def test_category_string_method(self):
        """
        Test that Categories return the correct string.
        """
        c = Category.objects.get(name="test_category")
        self.assertEqual(str(c), "test_category")

    def test_category_get_friendly_name_method(self):
        """
        Test that Categories return the correct friendly name.
        """
        c = Category.objects.get(name="test_category")
        self.assertEqual(c.get_friendly_name(), "Test Category")

    def test_tag_creation(self):
        """
        Test that Tags are created using the Tag
        model.
        """
        t = Tag.objects.get(name="test_tag")
        self.assertTrue(isinstance(t, Tag))

    def test_tag_string_method(self):
        """
        Test that Tags return the correct string.
        """
        t = Tag.objects.get(name="test_tag")
        self.assertEqual(str(t), "test_tag")

    def test_tag_get_friendly_name_method(self):
        """
        Test that Tags return the correct friendly name.
        """
        t = Tag.objects.get(name="test_tag")
        self.assertEqual(t.get_friendly_name(), "Test Tag")

    def test_product_creation(self):
        """
        Test that Products are created using the Product
        model.
        """
        p = Product.objects.get(name="test_product")
        self.assertTrue(isinstance(p, Product))

    def test_product_string_method(self):
        """
        Test that Products return the correct string.
        """
        p = Product.objects.get(name="test_product")
        self.assertEqual(str(p), "test_product")

    def test_product_get_friendly_name_method(self):
        """
        Test that Tags return the correct friendly name.
        """
        p = Product.objects.get(name="test_product")
        self.assertEqual(p.get_friendly_name(), "Test Product")

    def test_productimage_creation(self):
        """
        Test that ProductImage objects are created using the
        ProductImage model.
        """
        p = Product.objects.get(name="test_product")
        pi = ProductImage.objects.create(product=p, image="testimage.jpg")
        self.assertTrue(isinstance(pi, ProductImage))

    def test_productimage_string_method(self):
        """
        Test that ProductImages return the correct string.
        """
        p = Product.objects.get(name="test_product")
        pi = ProductImage.objects.create(product=p, image="testimage.jpg")
        self.assertEqual(str(pi), "test_product, testimage.jpg")

    def test_producttag_creation(self):
        """
        Test that ProductTag objects are created using the
        ProductTagmodel.
        """
        p = Product.objects.get(name="test_product")
        t = Tag.objects.get(name="test_tag")
        pt = ProductTag.objects.create(product=p, tag=t)
        self.assertTrue(isinstance(pt, ProductTag))

    def test_producttag_string_method(self):
        """
        Test that ProductTags return the correct string.
        """
        p = Product.objects.get(name="test_product")
        t = Tag.objects.get(name="test_tag")
        pt = ProductTag.objects.create(product=p, tag=t)
        self.assertEqual(str(pt), "test_product, test_tag")

    def test_productreview_creation(self):
        """
        Test that ProductReview objects are created using the
        ProductReview model.
        """
        p = Product.objects.get(name="test_product")
        pr = ProductReview.objects.create(
            product=p,
            review_rating=int(5),
            review_title="Test Review Title",
            review_content="Test Review Content"
        )
        self.assertTrue(isinstance(pr, ProductReview))

    def test_productreview_string_method(self):
        """
        Test that ProductReviews return the correct string.
        """
        p = Product.objects.get(name="test_product")
        pr = ProductReview.objects.create(
            product=p,
            review_rating=int(5),
            review_title="Test Review Title",
            review_content="Test Review Content"
        )
        self.assertEqual(str(pr), "5 stars, Test Review Title")
