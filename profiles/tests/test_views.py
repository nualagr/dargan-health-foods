from django.test import TestCase
from django.contrib.auth.models import User
from cart.models import DiscountCode
from django.test.client import Client


class TestProfileViews(TestCase):

    def setUp(self):
        """ Create a DiscountCode and User for the purposes of testing."""
        # Create the DiscountCode that is automatically assigned to new users
        discount_code = DiscountCode.objects.create(
            discount_code="NEW10",
            percentage_discount=10,
        )

        # Create a User for the tests
        self.client = Client()
        self.user = User.objects.create_user(
            "TestyTest",
            "testytest@test.com",
            "testerpassword",
        )

    def test_profile_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the profile page
        for a logged-in user.
        """
        self.client.login(
            username="TestyTest",
            password="testerpassword"
        )
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_view_not_logged_in(self):
        """
        Test profile view redirects to the login page
        when a user is not logged in.
        """
        response = self.client.get("/profile/")
        self.assertRedirects(response, "/accounts/login/?next=/profile/")
