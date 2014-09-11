from django.test import TestCase
from models import Cidade


# Create your tests here.
class CidadeTestCase(TestCase):
    def setUp(self):
        Cidade.objects.create(nome="Buritizeiro")

    def test_animals_can_speak(self):
        """Cliente that can speak are correctly identified"""
        cidade = Cidade.objects.get(nome="Buritizeiro")
        self.assertEqual(cidade.nome, 'Buritizeiro')
