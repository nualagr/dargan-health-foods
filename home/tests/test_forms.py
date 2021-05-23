from django.test import TestCase
from ..models import NewsletterSubscription
from ..forms import NewsletterSubscriptionForm, ContactForm
from django.utils import timezone


class NewsletterSubscriptionFormTest(TestCase):
    def test_valid_form(self):
        """
        Test NewsletterSubscriptionForm validation.
        """
        ns = NewsletterSubscription.objects.create(
            email_address="testemailaddress@test.com",
            date_subscribed=timezone.now(),
        )
        data = {
            "email_address": ns.email_address,
            "date_subscribed": timezone.now(),
        }
        form = NewsletterSubscriptionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_email_is_required(self):
        """
        Test whether the email_address field is required
        to successfully submit the NewsletterSubscriptionForm.
        """
        ns = NewsletterSubscription.objects.create(
            email_address="", date_subscribed=timezone.now()
        )
        data = {
            "email_address": ns.email_address,
            "date_subscribed": timezone.now(),
        }
        form = NewsletterSubscriptionForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("email_address", form.errors.keys())
        self.assertEqual(
            form.errors["email_address"][0],
            "This field is required."
        )


class ContactFormTest(TestCase):
    def test_valid_form(self):
        """
        Test the ContactForm validation process.
        """
        data = {
            "your_name": "Testy Test",
            "your_email": "testemailaddress@test.com",
            "your_message": "This form should be valid.",
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_name_is_required(self):
        """
        Test whether the name field is required
        to successfully submit the ContactForm.
        """
        form = ContactForm({"your_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("your_name", form.errors.keys())
        self.assertEqual(
            form.errors["your_name"][0],
            "This field is required."
        )

    def test_email_is_required(self):
        """
        Test whether the your_email field is required
        to successfully submit the ContactForm.
        """
        form = ContactForm({"your_email": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("your_email", form.errors.keys())
        self.assertEqual(form.errors["your_email"][0],
                         "This field is required.")

    def test_message_is_required(self):
        """
        Test whether the message field is required
        to successfully submit the ContactForm.
        """
        form = ContactForm({"your_message": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("your_message", form.errors.keys())
        self.assertEqual(
            form.errors["your_message"][0],
            "This field is required."
        )
