from django.test import TestCase


class TestHomeViews(TestCase):
    """
    Tests for views within the home app.
    """

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_our_story_view(self):
        response = self.client.get("/our_story/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/our_story.html")

    def test_contact_view(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/contact.html")
