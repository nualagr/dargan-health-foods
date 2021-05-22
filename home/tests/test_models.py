from django.test import TestCase
from ..models import NewsletterSubscription
from django.utils import timezone


class NewsletterSubscriptionTest(TestCase):
    def create_newslettersubscription(
        self,
        email_address="testemailaddress@test.com"
    ):
        """
        Function to create NewsletterSubscription for testing.
        """
        return NewsletterSubscription.objects.create(
            email_address=email_address, date_subscribed=timezone.now()
        )

    def test_newslettersubscription_creation(self):
        """
        Test the creation of a NewsletterSubscription.
        """
        ns = self.create_newslettersubscription()
        self.assertTrue(isinstance(ns, NewsletterSubscription))
        self.assertEqual("testemailaddress@test.com", ns.email_address)

    def test_newsletterscubscription_string_method(self):
        """
        Test that NewsletterSubscriptions return the correct string.
        """
        ns = self.create_newslettersubscription()
        self.assertEqual(str(ns), "testemailaddress@test.com")
