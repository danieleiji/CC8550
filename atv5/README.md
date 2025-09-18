# Projeto Prático: Testes de Unidade e Integração - Calculadora

Este projeto contém a implementação de testes de unidade e integração para uma classe `Calculadora` em Python, como parte de um exercício prático sobre qualidade de software e testes.

## Estrutura de Arquivos
O projeto está organizado da seguinte forma:

```
projeto_calculadora/
|-- src/
|   |-- calculadora.py       # Código fonte da classe Calculadora
|-- tests/
|   |-- __init__.py          # Arquivo para inicializar o pacote de testes
|   |-- test_unidade.py      # Testes de unidade para a Calculadora
|   |-- test_integracao.py   # Testes de integração para a Calculadora
|-- requirements.txt         # Dependências do projeto (coverage)
|-- README.md                # Este arquivo
```

## Como Executar

### 1. Preparação do Ambiente
Primeiro, clone o repositório e crie um ambiente virtual (recomendado):

```bash
git clone <url-do-seu-repositorio>
cd projeto_calculadora
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 2. Instalação das Dependências
Instale a biblioteca `coverage` para análise de cobertura de código:

```bash
pip install -r requirements.txt
```

### 3. Execução dos Testes
Para executar todos os testes (unidade e integração), use o `unittest discover`:

```bash
python -m unittest discover tests -v
```

### 4. Geração do Relatório de Cobertura
Para verificar a cobertura de testes do código fonte, execute os seguintes comandos:

```bash
# Executa os testes e coleta dados de cobertura
coverage run -m unittest discover tests

# Exibe o relatório no terminal
coverage report -m

# Gera um relatório HTML detalhado na pasta `htmlcov/`
coverage html
```
Abra o arquivo `htmlcov/index.html` em seu navegador para ver o relatório interativo.

---

## Relatório de Análise e Documentação

### Correções no Código Fonte

O código original da `Calculadora` continha pequenos bugs no registro do histórico de operações, que foram corrigidos:
1.  **`subtrair()`**: A string de formatação do histórico não incluía o operador `-`. Foi corrigido de `f"{a} = {b} {resultado}"` para `f"{a} - {b} = {resultado}"`.
2.  **`potencia()`**: A string do histórico não incluía o operador `**`. Foi corrigido de `f"{base} {expoente} = {resultado}"` para `f"{base} ** {expoente} = {resultado}"`.
3.  **Refatoração**: Um método privado `_verificar_operandos` foi adicionado para evitar a repetição do bloco de verificação de tipos em todas as funções públicas, melhorando a manutenibilidade do código.

### Resultados da Execução
Após a implementação de todos os testes solicitados e dos testes extras, a execução foi bem-sucedida.

**Saída esperada da execução dos testes:**
```
----------------------------------------------------------------------
Ran 23 tests in 0.002s

OK
```
**Saída esperada do relatório de cobertura:**
```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/__init__.py               0      0   100%
src/calculadora.py           39      0   100%
-------------------------------------------------------
TOTAL                        39      0   100%
```

### Lições Aprendidas sobre cada Tipo de Teste

*   **Testes de Entrada e Saída**: Essenciais para validar a funcionalidade principal. Garantem que, para uma entrada válida, a saída é exatamente a esperada.
*   **Testes de Tipagem**: Fundamentais em linguagens de tipagem dinâmica como Python. Eles protegem o sistema contra entradas de tipo incorreto que poderiam causar erros inesperados em tempo de execução.
*   **Testes de Consistência**: Verificam se o estado interno do objeto (`historico` e `resultado`) permanece correto e consistente após uma ou mais operações. São cruciais para objetos que mantêm estado.
*   **Testes de Inicialização**: Garantem que um objeto seja criado em um estado inicial válido e previsível, o que é a base para todas as operações subsequentes.
*   **Testes de Modificação de Dados**: Confirmam que métodos que alteram o estado do objeto (como `limpar_historico`) funcionam como esperado.
*   **Testes de Limite (Inferior/Superior)**: Exploram os extremos dos valores de entrada (zeros, números muito grandes/pequenos, limites de tipos de dados). Ajudam a encontrar bugs de overflow, underflow e comportamento inesperado em casos de borda.
*   **Testes de Valores Fora do Intervalo**: Validam o tratamento de erros para entradas que são semanticamente inválidas (como divisão por zero), garantindo que o sistema falhe de maneira graciosa e previsível.
*   **Testes de Fluxos de Controle**: Asseguram que todos os caminhos lógicos (ex: `if/else`) dentro de uma função sejam testados, tanto o caminho de sucesso quanto os de erro.
*   **Testes de Mensagens de Erro**: Verificam se as mensagens de erro são claras e informativas, o que é vital para a depuração e para o feedback ao usuário/desenvolvedor.
*   **Testes de Integração (Operações Sequenciais / Interface entre Métodos)**: Vão além do teste de unidades isoladas e verificam se diferentes partes do sistema colaboram corretamente. Eles simulam cenários de uso mais realistas, onde o resultado de uma operação se torna a entrada para a próxima.