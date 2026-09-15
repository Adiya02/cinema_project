from django.test import TestCase
from django.urls import reverse


class CinemaViewsTests(TestCase):

    def test_index_status_ok(self):
        response = self.client.get(reverse("cinema:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Онлайн-кинотеатр")

    def test_set_preferences_saves_cookies(self):
        response = self.client.post(
            reverse("cinema:set_preferences"),
            {"genre": "comedy", "theme": "dark", "language": "en"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.cookies["genre"].value, "comedy")
        self.assertEqual(response.cookies["theme"].value, "dark")
        self.assertEqual(response.cookies["language"].value, "en")

    def test_clear_preferences(self):
        self.client.cookies["genre"] = "action"
        response = self.client.get(reverse("cinema:clear_preferences"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("genre", response.cookies)

    def test_index_shows_selected_genre(self):
        self.client.cookies["genre"] = "action"
        response = self.client.get(reverse("cinema:index"))
        self.assertContains(response, "Боевики")
        self.assertContains(response, "Форсаж")