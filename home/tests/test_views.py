from django.test import TestCase


class TestHomeViews(TestCase):
    def test_index_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the index page.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_our_story_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the our_story page.
        """
        response = self.client.get("/our_story/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/our_story.html")

    def test_contact_view(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the contact page.
        """
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/contact.html")
