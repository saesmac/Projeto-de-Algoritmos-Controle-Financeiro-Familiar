import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# VARIÁVEIS GLOBAIS
renda_total = 0
renda1 = 0
renda2 = 0

# Lista de gastos
gastos = []

# indica a situação do canvas do grafico
canvas_grafico = None


# FUNÇÃO DO GRÁFICO
def atualizar_grafico():
    global canvas_grafico

    fig, ax = plt.subplots()
    valores = [renda1, renda2]
    nomes = ["Pessoa 1", "Pessoa 2"]

    ax.pie(valores, labels=nomes, autopct='%1.1f%%')
    ax.set_title("Proporção da Renda Bruta")

    # remove gráfico anterior se existir (evita duplicação na tela)
    if canvas_grafico is not None:
        canvas_grafico.get_tk_widget().destroy()

    canvas_grafico = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas_grafico.draw()
    canvas_grafico.get_tk_widget().pack()


# CALCULAR RENDA
def calcular_renda():
    global renda_total, renda1, renda2

    try:
        renda1 = float(entrada1.get())
        renda2 = float(entrada2.get())
        renda_total = renda1 + renda2

        label1.pack_forget()
        entrada1.pack_forget()
        label2.pack_forget()
        entrada2.pack_forget()
        botao_calcular.pack_forget()

        label_bruta.config(text=f"Renda bruta: R$ {renda_total:.2f}")
        label_restante.config(text=f"Renda restante: R$ {renda_total:.2f}")

        label_bruta.pack()
        label_restante.pack()

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

        if valor > renda_total:
            label_restante.config(text="Gasto maior que a renda restante!")
            return

        proporcao1 = renda1 / (renda1 + renda2)
        proporcao2 = renda2 / (renda1 + renda2)

        paga1 = valor * proporcao1
        paga2 = valor * proporcao2

        renda_total -= valor

        label_restante.config(text=f"Renda restante: R$ {renda_total:.2f}")

        gastos.append([descricao, valor, paga1, paga2])

        historico.delete(1.0, tk.END)

        for gasto in gastos:
            historico.insert(
                tk.END,
                f"{gasto[0]}: -R$ {gasto[1]:.2f}\n"
                f"Pessoa 1 paga: R$ {gasto[2]:.2f}\n"
                f"Pessoa 2 paga: R$ {gasto[3]:.2f}\n\n"
            )

        entrada_gasto.delete(0, tk.END)
        entrada_desc.delete(0, tk.END)

    except ValueError:
        label_restante.config(text="Erro no valor do gasto!")


# LIMPAR HISTÓRICO
def limpar_historico():
    global gastos
    gastos = []
    historico.delete(1.0, tk.END)


# BOTÃO VOLTAR (RESET TOTAL)
def voltar_inicio():
    global renda_total, renda1, renda2, gastos, canvas_grafico

    # zera todas as variáveis do sistema
    renda_total = 0
    renda1 = 0
    renda2 = 0
    gastos = []

    # limpa histórico da tela
    historico.delete(1.0, tk.END)

    # limpa gráfico da tela
    if canvas_grafico is not None:
        canvas_grafico.get_tk_widget().destroy()
        canvas_grafico = None

    # reseta labels
    label_bruta.config(text="")
    label_restante.config(text="")

    # volta interface inicial 
    label1.pack()
    entrada1.pack()
    label2.pack()
    entrada2.pack()
    botao_calcular.pack(pady=10)

    # esconde campos de gasto 
    label_gasto.pack_forget()
    entrada_gasto.pack_forget()
    label_desc.pack_forget()
    entrada_desc.pack_forget()
    botao_subtrair.pack_forget()


# INTERFACE
janela = tk.Tk()
janela.title("Controle Financeiro Familiar")
janela.configure(background="#f2f4f7")
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
label1 = tk.Label(frame_esquerda, text="💰 Renda pessoa 1:")
label1.pack()

entrada1 = tk.Entry(frame_esquerda)
entrada1.pack()

label2 = tk.Label(frame_esquerda, text="💰 Renda pessoa 2:")
label2.pack()

entrada2 = tk.Entry(frame_esquerda)
entrada2.pack()

# BOTÃO CALCULAR
botao_calcular = tk.Button(
    frame_esquerda,
    text="Calcular",
    command=calcular_renda,
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    relief="flat",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
    cursor="hand2"
)
botao_calcular.pack(pady=10)

# CAMPOS DE GASTO
label_gasto = tk.Label(frame_esquerda, text="💸 Valor do gasto:")
entrada_gasto = tk.Entry(frame_esquerda)

label_desc = tk.Label(frame_esquerda, text="🧾 Descrição:")
entrada_desc = tk.Entry(frame_esquerda)

botao_subtrair = tk.Button(
    frame_esquerda,
    text="Adicionar gasto",
    command=subtrair_gasto,
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    relief="flat",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
    cursor="hand2"
)

# HISTÓRICO
historico_label = tk.Label(frame_direita, text="🧾 Histórico de Gastos:")
historico_label.pack()

historico = tk.Text(frame_direita, height=18, width=35)
historico.pack()

frame_botoes = tk.Frame(frame_direita)
frame_botoes.pack(pady=10)

botao_voltar = tk.Button(
    frame_botoes,
    text="⬅ Voltar (Reset)",
    command=voltar_inicio,  
    bg="#7f8c8d",
    fg="white",
    activebackground="#5f6a6a",
    relief="flat",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
    cursor="hand2"
)
botao_voltar.pack(side="left", padx=5)

# BOTÃO LIMPAR
botao_limpar = tk.Button(
    frame_botoes,
    text="🗑 Limpar",
    command=limpar_historico,
    bg="#e74c3c",
    fg="white",
    activebackground="#c0392b",
    relief="flat",
    padx=10,
    pady=5,
    cursor="hand2"
)
botao_limpar.pack(side="left", padx=5)

janela.mainloop()
