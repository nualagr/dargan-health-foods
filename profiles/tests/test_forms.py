from django.test import TestCase
from ..forms import DargansCustomSignupForm, UserProfileForm


class TestDargansCustomSignupForm(TestCase):
    def test_valid_form(self):
        """
        Test DargansCustomSignupForm validation.
        """
        form = DargansCustomSignupForm(
            {
                "email": "testytest@example.com",
                "email2": "testytest@example.com",
                "username": "TestyTest",
                "first_name": "Testy",
                "last_name": "Test",
                "password1": "testpassword",
                "password2": "testpassword",
            }
        )
        self.assertTrue(form.is_valid())

    def test_fields_are_required(self):
        """
        Test that every field within the
        DargansCustomSignupForm is required.
        """
        form = DargansCustomSignupForm(
            {
                "email": "",
                "email2": "",
                "username": "",
                "first_name": "",
                "last_name": "",
                "password1": "",
                "password2": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"][0], "This field is required.")
        self.assertEqual(form.errors["email2"][0], "This field is required.")
        self.assertEqual(form.errors["username"][0], "This field is required.")
        self.assertEqual(
            form.errors["first_name"][0], "This field is required."
        )
        self.assertEqual(
            form.errors["last_name"][0], "This field is required."
        )
        self.assertEqual(
            form.errors["password1"][0], "This field is required."
        )
        self.assertEqual(
            form.errors["password2"][0], "This field is required."
        )


class TestUserProfileForm(TestCase):
    def test_valid_form(self):
        """
        Test UserProfileForm validation.
        """
        form = UserProfileForm({"default_phone_number": "01555555"})
        self.assertTrue(form.is_valid())
