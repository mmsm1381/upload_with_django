from os import name
from django.forms import FileField
from django.test import TestCase


from .models import Flile


class TestFileModel(TestCase):

    def setUp(self) -> None:
        Flile.objects.create(name="test")

    def test_file_model(self):
        file = Flile.objects.get(name="test")
        self.assertEqual(print(file),file.name,"file str and name are not == ")


