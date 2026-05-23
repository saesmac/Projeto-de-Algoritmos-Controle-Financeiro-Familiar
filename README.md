# Controle Financeiro Familiar

Sistema desktop desenvolvido em Python com interface gráfica para auxiliar no gerenciamento financeiro familiar, permitindo controle de renda, divisão proporcional de despesas, histórico de gastos e visualização gráfica das contribuições financeiras.

---

# Sobre o Projeto

O projeto foi desenvolvido para a disciplina de Algoritmos com o objetivo de aplicar conceitos fundamentais de programação através de uma solução prática e útil para o cotidiano.

O sistema permite que duas pessoas registrem suas rendas e realizem o controle compartilhado das despesas da casa, dividindo automaticamente os gastos de forma proporcional à renda de cada uma.

Além disso, o programa gera um gráfico de pizza para representar visualmente a participação financeira de cada pessoa.

---

# Objetivos

- Aplicar conceitos de lógica de programação.
- Trabalhar com estruturas de repetição e decisão.
- Utilizar listas (vetores) para armazenamento de dados.
- Desenvolver uma interface gráfica funcional.
- Manipular dados financeiros de forma prática.
- Gerar visualizações gráficas utilizando Python.

---

# Funcionalidades

## Cadastro de renda

O usuário informa:
- renda da pessoa 1
- renda da pessoa 2

O sistema calcula automaticamente:
- renda total da família
- renda restante disponível

---

## Divisão proporcional de gastos

Cada gasto é dividido proporcionalmente conforme a renda de cada pessoa.

### Exemplo:

| Pessoa | Renda |
|---|---|
| Pessoa 1 | R$ 3000 |
| Pessoa 2 | R$ 1000 |

Se um gasto for de R$ 400:
- Pessoa 1 paga R$ 300
- Pessoa 2 paga R$ 100

---

## Histórico de despesas

Todos os gastos ficam registrados no sistema contendo:
- descrição
- valor total
- valor pago por cada pessoa

---

## Gráfico de pizza

O sistema gera automaticamente um gráfico representando:
- porcentagem da renda da pessoa 1
- porcentagem da renda da pessoa 2

---

## Interface gráfica

A aplicação possui interface desenvolvida com Tkinter, tornando o sistema mais intuitivo e interativo.

---

# Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Python | Linguagem principal |
| Tkinter | Interface gráfica |
| Matplotlib | Geração de gráficos |

---

# Conceitos de Algoritmos Aplicados

Durante o desenvolvimento foram utilizados diversos conceitos estudados na disciplina:

- Variáveis
- Entrada e saída de dados
- Estruturas condicionais
- Estruturas de repetição
- Funções
- Vetores/Listas
- Manipulação de dados
- Interface gráfica
- Organização modular do código

---

# Estrutura do Projeto

```text
Projeto-de-Algoritmos-Controle-Financeiro-Familiar/
│
├── interface2.py
└── README.md
```

---

# Como Executar o Projeto

## 1️: Instalar o Python

Baixe e instale o Python:

https://www.python.org/downloads/

---

## 2️: Instalar as dependências

Abra o terminal na pasta do projeto e execute:

```bash
pip install matplotlib
```

---

## 3: Executar o sistema

No terminal, execute:

```bash
python interface2.py
```

---

# Funcionamento do Sistema

## Etapa 1 — Cadastro das rendas

O usuário informa:
- renda da pessoa 1
- renda da pessoa 2

O sistema calcula automaticamente a renda bruta total.

---

## Etapa 2 — Adição de gastos

O usuário informa:
- valor do gasto
- descrição

O sistema:
- subtrai o valor da renda restante
- divide proporcionalmente entre as pessoas
- salva no histórico

---

## Etapa 3 — Visualização do histórico

O histórico exibe:
- nome do gasto
- valor total
- quanto cada pessoa deve pagar

---

## Etapa 4 — Gráfico financeiro

O gráfico de pizza mostra visualmente a proporção das rendas.

---

# Exemplo de Uso

### Entrada:

- Pessoa 1: R$ 3000
- Pessoa 2: R$ 2000
- Gasto: Mercado — R$ 500

### Resultado:

- Pessoa 1 paga: R$ 300
- Pessoa 2 paga: R$ 200

---

# Melhorias Futuras

- Salvamento em banco de dados
- Exportação de relatórios em PDF
- Sistema de login
- Integração com APIs bancárias
- Controle mensal de despesas
- Gráficos avançados
- Categorias de gastos
- Modo escuro

---

# Integrantes do Grupo

- Daniel Koyama
- Eduardo Saes
- Lucas Martins
- Nicoly Oliveira
- Yasmin Miranda

---

# Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de Algoritmos.

---

# Considerações Finais

O projeto permitiu aplicar na prática conceitos importantes de programação e desenvolvimento de interfaces gráficas, além de demonstrar como algoritmos podem ser utilizados para resolver problemas reais do cotidiano financeiro.
