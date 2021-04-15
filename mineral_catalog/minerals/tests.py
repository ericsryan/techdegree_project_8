from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class ModelTests(TestCase):
    def setUp(self):
        mineral = Mineral.objects.create(
            name="Test",
            caption="Hi"
        )
        mineral = Mineral.objects.create(
            name="Test",
            caption="Bye"
        )

    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Mineral",
            caption="Hi"
        )
        self.assertEqual(mineral.name, "Mineral")

    def test_mineral_slug(self):
        mineral = Mineral.objects.get(caption="Hi")
        mineral2 = Mineral.objects.get(caption="Bye")
        self.assertEqual(mineral.slug, 'test')
        self.assertEqual(mineral2.slug, 'test-2')

    def test_model_str(self):
        mineral = Mineral.objects.get(caption="Hi")
        self.assertEqual(mineral.__str__(), mineral.name)


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Test",
            caption="Hi"
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertContains(resp, self.mineral.name)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('detail',
                                       kwargs={'pk':self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertContains(resp, self.mineral.name)

    def test_random_mineral_view(self):
        resp = self.client.get(reverse('random'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    def test_mineral_list_by_color_view(self):
        resp = self.client.get(reverse('mineral_list_by_color',
                                       kwargs={'color': 'Blue'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_mineral_list_by_group_view(self):
        resp = self.client.get(reverse('mineral_list_by_group',
                                       kwargs={'group': 'Silicates'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_mineral_list_by_letter_view(self):
        resp = self.client.get(reverse('mineral_list_by_letter',
                                       kwargs={'letter': 'T'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_search_minerals_view(self):
        resp = self.client.get(reverse('search'), {'query': 'Test'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)


if __name__ == '__main__':
    unittest.main()
