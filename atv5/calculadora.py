# src/calculadora.py
import math

class Calculadora:
    """
    Uma calculadora simples que realiza operações básicas e mantém um histórico.
    """
    def __init__(self):
        """Inicializa a calculadora com histórico vazio e resultado zerado."""
        self.historico = []
        self.resultado = 0

    def _verificar_operandos(self, *args):
        """Método auxiliar para verificar se todos os operandos são números."""
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Argumentos devem ser numeros")

    def somar(self, a, b):
        """Soma dois números e registra a operação."""
        self._verificar_operandos(a, b)
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def subtrair(self, a, b):
        """Subtrai dois números e registra a operação."""
        self._verificar_operandos(a, b)
        resultado = a - b
        # CORREÇÃO: O operador estava faltando na string do histórico.
        self.historico.append(f"{a} - {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def multiplicar(self, a, b):
        """Multiplica dois números e registra a operação."""
        self._verificar_operandos(a, b)
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def dividir(self, a, b):
        """Divide dois números, com tratamento para divisão por zero."""
        self._verificar_operandos(a, b)
        if b == 0:
            raise ValueError("Divisao por zero nao permitida")
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def potencia(self, base, expoente):
        """Calcula a potência de um número."""
        self._verificar_operandos(base, expoente)
        resultado = base ** expoente
        # CORREÇÃO: O operador estava faltando na string do histórico.
        self.historico.append(f"{base} ** {expoente} = {resultado}")
        self.resultado = resultado
        return resultado

    def limpar_historico(self):
        """Limpa o histórico de operações."""
        self.historico.clear()

    def obter_ultimo_resultado(self):
        """Retorna o último resultado calculado."""
        return self.resultado