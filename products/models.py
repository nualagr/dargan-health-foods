from django.db import models
from profiles.models import UserProfile


class Department(models.Model):
    """
    Creates a Department model containing the names of
    overarching product-category departments
    """

    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):
    """
    Creates a Category model containing the names of
    product categories and their related department id
    """

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="categories",
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """
    Creates a Brand model containing the names of
    product brands
    """

    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tag(models.Model):
    """
    Creates a Tag model containing the tags
    commonly used to identify subcategories of
    products or blog posts.
    """

    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=80)
    friendly_name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Creates a Product model containing data about each individual
    product
    """

    class Meta:
        ordering = ["sku"]

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    abbreviated_friendly_name = models.CharField(
        max_length=80, null=True, blank=True
    )
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="products_brand",
    )
    size_value = models.PositiveSmallIntegerField(
        default=0, null=True, blank=True
    )
    size_unit = models.CharField(max_length=10, null=True, blank=True)
    weight_g = models.PositiveSmallIntegerField(
        default=0, null=True, blank=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_offer = models.BooleanField(default=False, null=True, blank=True)
    discount_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    vat_code = models.CharField(max_length=3, null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    free_from = models.BooleanField(default=False, null=True, blank=True)
    allergens = models.TextField(blank=True)
    usage = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="products_category",
    )
    barcode = models.CharField(max_length=13, null=True, blank=True)
    avg_rating = models.DecimalField(
        max_digits=2, decimal_places=1, default=0, null=True, blank=True
    )
    date_added = models.DateTimeField(auto_now_add=True)
    num_in_stock = models.PositiveIntegerField(
        default=0, null=True, blank=True
    )
    discontinued = models.BooleanField(default=False, null=True, blank=True)
    main_image = models.ImageField(
        upload_to="product_images", null=True, blank=True
    )
    main_image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductImage(models.Model):
    """
    Creates a ProductImage model containing
    the image and image url for each product.
    """

    class Meta:
        ordering = ["product"]

    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="productimages",
    )
    image = models.ImageField(
        upload_to="product_images", null=True, blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.product, self.image)


class ProductTag(models.Model):
    class Meta:
        ordering = ["product"]

    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="producttags",
    )
    tag = models.ForeignKey(
        Tag,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="tagproducts",
    )

    def __str__(self):
        return "{}, {}".format(self.product, self.tag)


class ProductReview(models.Model):
    class Meta:
        ordering = ["product"]

    STAR_RATING_CHOICES = (
        (1, "⭐"),
        (2, "⭐ ⭐"),
        (3, "⭐ ⭐ ⭐"),
        (4, "⭐ ⭐ ⭐ ⭐"),
        (5, "⭐ ⭐ ⭐ ⭐ ⭐"),
    )
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="productreviews",
    )
    user = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="usersreviews",
    )
    review_rating = models.IntegerField(choices=STAR_RATING_CHOICES)
    review_title = models.CharField(max_length=255)
    review_content = models.TextField()
    created = models.DateField(auto_now_add=True, editable=False)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return "{} stars, {}".format(self.review_rating, self.review_title)
