from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from ..models import UserProfile, DiscountCode2User
from cart.models import DiscountCode


class TestProfilesModels(TestCase):
    def setUp(self):
        """
        Create a DiscountCode, User and UserProfile for
        testing purposes.
        """
        self.dc = DiscountCode.objects.create(
            discount_code="NEW10", percentage_discount=0.1
        )
        self.client = Client()
        self.user = User.objects.create_user(
            "TestyTest",
            "testytest@test.com",
            "testerpassword",
        )
        self.up = UserProfile.objects.get(user=self.user)

    def test_userprofile_creation(self):
        """
        Test that UserProfiles are created using the UserProfile
        model.
        """
        self.assertTrue(isinstance(self.up, UserProfile))

    def test_userprofile_string_method(self):
        """
        Test that UserProfiles return the correct string.
        """
        self.assertEqual(str(self.up), "TestyTest")

    def test_discountcode2user_creation(self):
        """
        Test whether DiscountCode2User objects are created using the
        DiscountCode2User model.
        Test whether the DiscountCode2User returns
        the related DiscountCode.
        """
        dc2u = DiscountCode2User.objects.create(
            user=self.up, discount_code=self.dc
        )
        self.assertTrue(isinstance(dc2u, DiscountCode2User))
        self.assertEqual("NEW10", dc2u.discount_code.discount_code)

    def test_discountcode2user_string_method(self):
        """
        Test that DiscountCode2User objects return the correct string.
        """
        dc2u = DiscountCode2User.objects.create(
            user=self.up, discount_code=self.dc
        )
        self.assertEqual(
            str(dc2u),
            "TestyTest's PromoCode: NEW10, Valid: True",
        )
