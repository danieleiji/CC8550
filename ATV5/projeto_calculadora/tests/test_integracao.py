# tests/test_integracao.py
import unittest
from src.calculadora import Calculadora

class TestCalculadoraIntegracao(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()

    # 4.1 Teste de Operações Sequenciais
    def test_operacoes_sequenciais(self):
        self.calc.somar(2, 3)
        resultado1 = self.calc.obter_ultimo_resultado()
        self.assertEqual(resultado1, 5)

        self.calc.multiplicar(resultado1, 4)
        resultado2 = self.calc.obter_ultimo_resultado()
        self.assertEqual(resultado2, 20)

        self.calc.dividir(resultado2, 2)
        resultado_final = self.calc.obter_ultimo_resultado()
        
        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(self.calc.historico), 3)

    def test_operacoes_sequenciais_com_subtracao_e_potencia(self):
        self.calc.subtrair(10, 2)
        res1 = self.calc.obter_ultimo_resultado()
        self.assertEqual(res1, 8)
        
        self.calc.potencia(res1, 2)
        res2 = self.calc.obter_ultimo_resultado()
        self.assertEqual(res2, 64)
        self.assertIn("10 - 2 = 8", self.calc.historico)
        self.assertIn("8 ^ 2 = 64", self.calc.historico)
        
    # 4.2 Teste de Interface entre Métodos
    def test_integracao_historico_resultado(self):
        self.calc.potencia(2, 3)
        self.calc.somar(self.calc.obter_ultimo_resultado(), 2) 

        self.assertEqual(self.calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(self.calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", self.calc.historico)
        self.assertIn("8 + 2 = 10", self.calc.historico)
    
    def test_integracao_limpar_historico_no_meio_das_operacoes(self):
        self.calc.somar(10, 20)
        self.assertEqual(len(self.calc.historico), 1)
        self.assertEqual(self.calc.resultado, 30)
        
        self.calc.limpar_historico()
        self.assertEqual(len(self.calc.historico), 0)
        
        self.calc.multiplicar(5, 5)
        self.assertEqual(len(self.calc.historico), 1)
        self.assertEqual(self.calc.resultado, 25)
        self.assertNotIn("10 + 20 = 30", self.calc.historico)
        self.assertIn("5 * 5 = 25", self.calc.historico)