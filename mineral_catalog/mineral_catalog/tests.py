from django.urls import reverse
from django.test import TestCase

from minerals.models import Mineral, Attribute


class ModelTests(TestCase):
    def setUp(self):
        mineral = Mineral.objects.create(
            name="Test",
            caption="Hi"
        )

    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Mineral",
            caption="Hi"
        )
        self.assertEqual(mineral.name, "Mineral")

    def test_attribute_creation(self):
        attribute = Attribute.objects.create(
            name="category",
            content="Mineral",
            mineral=Mineral.objects.get(name="Test")
        )
        self.assertEqual(attribute.name, "category")


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Test",
            caption="Hi"
        )
        for i in range(3):
            attribute = Attribute.objects.create(
                name="category{}".format(i),
                content="Mineral",
                mineral=Mineral.objects.get(name="Test")
            )

    def test_index_view(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('detail',
                                       kwargs={'pk':self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])

    def test_random_mineral_view(self):
        resp = self.client.get(reverse('random'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/random_mineral_detail.html')
