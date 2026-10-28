from django.test import TestCase


class SimpleTestCase(TestCase):

  def test_basic_assertion(self):
    self.assertTrue(True)

