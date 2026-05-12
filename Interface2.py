import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# VARIÁVEIS GLOBAIS

renda_total = 0
renda1 = 0
renda2 = 0

# Vetor para armazenar gastos
gastos = []

# FUNÇÃO DO GRÁFICO

def atualizar_grafico():

    # Remove gráfico antigo
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots()

    valores = [renda1, renda2]
    nomes = ["Pessoa 1", "Pessoa 2"]

    # Evita erro se tudo for zero
    if renda1 == 0 and renda2 == 0:
        valores = [1, 1]

    # Cria gráfico de pizza
    ax.pie(valores, labels=nomes, autopct='%1.1f%%')

    ax.set_title("Proporção da Renda Bruta")

    # Coloca gráfico no Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

# CALCULAR RENDA

def calcular_renda():

    global renda_total, renda1, renda2

    try:

        # Entrada de dados
        renda1 = float(entrada1.get())
        renda2 = float(entrada2.get())

        # Soma das rendas
        renda_total = renda1 + renda2

        # Remove campos iniciais
        label1.pack_forget()
        entrada1.pack_forget()

        label2.pack_forget()
        entrada2.pack_forget()

        botao_calcular.pack_forget()

        # Mostra resultados
        label_bruta.config(text=f"Renda bruta: R$ {renda_total:.2f}")
        label_restante.config(text=f"Renda restante: R$ {renda_total:.2f}")

        label_bruta.pack()
        label_restante.pack()

        # Mostra área de gastos
        label_gasto.pack()
        entrada_gasto.pack()

        label_desc.pack()
        entrada_desc.pack()

        botao_subtrair.pack(pady=10)

        atualizar_grafico()

    except ValueError:

        label_bruta.config(text="Digite valores válidos!")

# ADICIONAR GASTO

def subtrair_gasto():

    global renda_total

    try:

        valor = float(entrada_gasto.get())
        descricao = entrada_desc.get()

        # Estrutura de decisão
        if valor > renda_total:

            label_restante.config(
                text="Gasto maior que a renda restante!"
            )

            return

        # Proporções
        proporcao1 = renda1 / (renda1 + renda2)
        proporcao2 = renda2 / (renda1 + renda2)

        # Divisão proporcional
        paga1 = valor * proporcao1
        paga2 = valor * proporcao2

        # Atualiza renda
        renda_total -= valor

        label_restante.config(
            text=f"Renda restante: R$ {renda_total:.2f}"
        )

        # Armazena no vetor
        gastos.append([
            descricao,
            valor,
            paga1,
            paga2
        ])

        # Limpa histórico
        historico.delete(1.0, tk.END)

        # Estrutura de repetição
        for gasto in gastos:

            texto = (
                f"{gasto[0]}: -R$ {gasto[1]:.2f}\n"
                f"Pessoa 1 paga: R$ {gasto[2]:.2f}\n"
                f"Pessoa 2 paga: R$ {gasto[3]:.2f}\n\n"
            )

            historico.insert(tk.END, texto)

        # Limpa campos
        entrada_gasto.delete(0, tk.END)
        entrada_desc.delete(0, tk.END)

    except ValueError:

        label_restante.config(
            text="Erro no valor do gasto!"
        )

# LIMPAR HISTÓRICO

def limpar_historico():

    global gastos

    gastos = []

    historico.delete(1.0, tk.END)

# INTERFACE

janela = tk.Tk()

janela.title("Controle Financeiro Familiar")

janela.geometry("1000x450")

# FRAMES

frame_esquerda = tk.Frame(janela)
frame_esquerda.pack(side="left", padx=20)

frame_direita = tk.Frame(janela)
frame_direita.pack(side="left", padx=20)

frame_grafico = tk.Frame(janela)
frame_grafico.pack(side="right", padx=20)

# LABELS

label_bruta = tk.Label(frame_esquerda, text="")
label_restante = tk.Label(frame_esquerda, text="")

# ENTRADAS

label1 = tk.Label(
    frame_esquerda,
    text="Renda pessoa 1:"
)

label1.pack()

entrada1 = tk.Entry(frame_esquerda)
entrada1.pack()

label2 = tk.Label(
    frame_esquerda,
    text="Renda pessoa 2:"
)

label2.pack()

entrada2 = tk.Entry(frame_esquerda)
entrada2.pack()

# BOTÃO CALCULAR

botao_calcular = tk.Button(
    frame_esquerda,
    text="Calcular",
    command=calcular_renda
)

botao_calcular.pack(pady=10)

# CAMPOS DE GASTO

label_gasto = tk.Label(
    frame_esquerda,
    text="Valor do gasto:"
)

entrada_gasto = tk.Entry(frame_esquerda)

label_desc = tk.Label(
    frame_esquerda,
    text="Descrição:"
)

entrada_desc = tk.Entry(frame_esquerda)

botao_subtrair = tk.Button(
    frame_esquerda,
    text="Adicionar gasto",
    command=subtrair_gasto
)

# HISTÓRICO

historico_label = tk.Label(
    frame_direita,
    text="Histórico de Gastos:"
)

historico_label.pack()

historico = tk.Text(
    frame_direita,
    height=18,
    width=35
)

historico.pack()

# BOTÃO LIMPAR

botao_limpar = tk.Button(
    frame_direita,
    text="Limpar Histórico",
    command=limpar_historico
)

botao_limpar.pack(pady=10)

# LOOP PRINCIPAL
janela.mainloop()