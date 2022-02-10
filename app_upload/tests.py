from django.test import TestCase


from .models import Flile


class TestFileModel(TestCase):

    def setUp(self) -> None:
        Flile.objects.create(body="user/files/facade_BGUvUU3.md",name="test")

    def test_file_size(self):
        file = Flile.objects.get(name="test")
        self.assertEqual(file.set_file_size(),file.body.size,"size are not ==")


