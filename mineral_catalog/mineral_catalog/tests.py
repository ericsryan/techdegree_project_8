from django.urls import reverse
from django.test import TestCase

from minerals.models import Mineral


class MineralCatalogViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Test",
            caption="Hi"
        )

    def test_index_view(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
