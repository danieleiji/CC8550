# tests/test_unidade.py
import unittest
import sys
from src.calculadora import Calculadora

class TestCalculadoraUnidade(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    # 3.1 Testes de Entrada e Saída
    def test_entrada_saida_soma(self):
        resultado = self.calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    def test_entrada_saida_subtracao(self):
        resultado = self.calc.subtrair(10, 4)
        self.assertEqual(resultado, 6)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 6)

    def test_entrada_saida_multiplicacao(self):
        resultado = self.calc.multiplicar(3, 7)
        self.assertEqual(resultado, 21)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 21)
        
    def test_entrada_saida_divisao(self):
        resultado = self.calc.dividir(20, 5)
        self.assertEqual(resultado, 4)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 4)

    def test_entrada_saida_potencia(self):
        resultado = self.calc.potencia(2, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    # 3.2 Testes de Tipagem
    def test_tipagem_invalida_geral(self):
        operacoes = [self.calc.somar, self.calc.subtrair, self.calc.multiplicar, self.calc.dividir, self.calc.potencia]
        invalidos = [("5", 3), (10, None), ([], 2), ({}, 1)]
        
        for op in operacoes:
            for a, b in invalidos:
                with self.assertRaises(TypeError, msg=f"Falhou em {op.__name__} com ({a}, {b})"):
                    op(a, b)

    def test_tipagem_segundo_argumento_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.somar(5, "3")

    # 3.3 Testes de Consistência
    def test_consistencia_historico(self):
        self.calc.somar(2, 3)
        self.calc.multiplicar(4, 5)
        self.assertEqual(len(self.calc.historico), 2)
        self.assertIn("2 + 3 = 5", self.calc.historico)
        self.assertIn("4 * 5 = 20", self.calc.historico)

    def test_consistencia_resultado(self):
        self.calc.somar(10, 5)
        self.assertEqual(self.calc.resultado, 15)
        self.calc.subtrair(self.calc.resultado, 5)
        self.assertEqual(self.calc.resultado, 10)

    # 3.4 Testes de Inicialização
    def test_inicializacao(self):
        self.assertEqual(self.calc.resultado, 0)
        self.assertEqual(len(self.calc.historico), 0)

    def test_inicializacao_tipo_objeto(self):
        self.assertIsInstance(self.calc, Calculadora)

    # 3.5 Testes de Modificação de Dados
    def test_modificacao_historico(self):
        self.calc.somar(1, 1)
        self.assertEqual(len(self.calc.historico), 1)
        self.calc.limpar_historico()
        self.assertEqual(len(self.calc.historico), 0)

    def test_modificacao_acumulativa_historico(self):
        self.calc.somar(1, 1)
        self.assertEqual(len(self.calc.historico), 1)
        self.calc.subtrair(2, 1)
        self.assertEqual(len(self.calc.historico), 2)

    # 3.6 Testes de Limite Inferior
    def test_limite_inferior(self):
        resultado_zero = self.calc.somar(0, 5)
        self.assertEqual(resultado_zero, 5)
        resultado_neg = self.calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado_neg, -2e-10)

    def test_limite_inferior_negativos(self):
        resultado = self.calc.somar(-100, -200)
        self.assertEqual(resultado, -300)

    # 3.7 Testes de Limite Superior
    def test_limite_superior(self):
        resultado = self.calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)
        
    def test_limite_float_max(self):
        max_float = sys.float_info.max
        resultado = self.calc.multiplicar(max_float, 1)
        self.assertEqual(resultado, max_float)
        with self.assertRaises(OverflowError):
             self.calc.potencia(max_float, 2)

    def test_limite_superior_multiplicacao(self):
        resultado = self.calc.multiplicar(1e150, 1e150)
        self.assertAlmostEqual(resultado / 1e300, 1.0, places=2)

    # 3.8 Testes de Valores Fora do Intervalo
    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
    
    def test_potencia_negativa_com_expoente_fracionario(self):
        with self.assertRaises(ValueError):
            self.calc.potencia(-4, 0.5)

    # 3.9 Testes de Fluxos de Controle
    def test_fluxos_divisao(self):
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_fluxos_soma(self):
        resultado = self.calc.somar(1, 1)
        self.assertEqual(resultado, 2)
        with self.assertRaises(TypeError):
            self.calc.somar(1, "1")

    # 3.10 Testes de Mensagens de Erro
    def test_mensagens_erro_divisao(self):
        with self.assertRaises(ValueError) as cm:
            self.calc.dividir(5, 0)
        self.assertEqual(str(cm.exception), "Divisao por zero nao permitida")

    def test_mensagens_erro_tipagem(self):
        with self.assertRaises(TypeError) as cm:
            self.calc.subtrair("a", 5)
        self.assertEqual(str(cm.exception), "Argumentos devem ser numeros")