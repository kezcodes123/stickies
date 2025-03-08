from django.test import TestCase
from django.urls import reverse
from .models import Sticky


class StickyViewsTestCase(TestCase):
    def setUp(self):
        self.sticky = Sticky.objects.create(
            name="Test Sticky",
            description="Test Description"
        )

    def test_get_all(self):
        response = self.client.get(reverse('sticky_list'))
        self.assertTemplateUsed(response, 'stickies/index.html')
        self.assertContains(response, "Test Sticky")

    def test_get(self):
        response = self.client.get(
            reverse('sticky_view', args=[self.sticky.pk])
        )
        self.assertTemplateUsed(response, 'stickies/detail.html')
        self.assertContains(response, "Test Sticky")

    def test_create(self):
        self.client.post(
            reverse('create_sticky'),
            {'name': 'New Sticky', 'description': 'New Description'}
        )
        self.assertTrue(Sticky.objects.filter(name='New Sticky').exists())

    def test_update(self):
        self.client.post(
            reverse('edit_sticky', args=[self.sticky.pk]),
            {'name': 'Updated Sticky', 'description': 'Updated Description'}
        )
        self.sticky.refresh_from_db()
        self.assertEqual(self.sticky.name, 'Updated Sticky')

    def test_delete(self):
        self.client.post(reverse('delete_sticky', args=[self.sticky.pk]))
        self.assertFalse(Sticky.objects.filter(pk=self.sticky.pk).exists())
