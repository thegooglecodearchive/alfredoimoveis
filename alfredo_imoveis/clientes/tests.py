from django.test import TestCase
from models import Cliente
from datetime import date


class ClienteTestCase(TestCase):

    def setUp(self):
        Cliente.objects.create(
            nome="lion", naturalidade_id=1, endereco_id=1,
            nome_pai='Pai teste', nome_mae='Mae teste', telefone_fixo='65468',
            profissao='Analista de Sistemas', nacionalidade=1,
            orgao_expeditor='SSP', data_nascimento=date.today(),
            cnpj_cpf='651', rg='351', email='asdfs@afddsa.com')

    def test_animals_can_speak(self):
        """Cliente that can speak are correctly identified"""
        cliente = Cliente.objects.get(nome="lion")
        self.assertEqual(cliente.nome, 'lion')
