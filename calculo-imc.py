import tkinter as tk
from tkinter import Label, Entry, Button, messagebox


def mostrar_mensagem():
    nome = txt_nome.get()
    try:
        peso = float(txt_peso.get())
        altura_cm = float(txt_altura.get())
        altura_m = altura_cm / 100
        calculo_imc = peso / (altura_m * altura_m)
        lbl_resultado["text"] = f"Seu nome é {nome} e seu IMC: {calculo_imc:.2f}"
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos para peso e altura.")

    if calculo_imc < 18.5:
        lbl_resultado["text"] = f"Seu nome é {nome} e seu IMC: {calculo_imc:.2f} - Abaixo do peso"
    elif calculo_imc >= 18.5 and calculo_imc <= 24.9:
        lbl_resultado["text"] = f"Seu nome é {nome} e seu IMC: {calculo_imc:.2f} - Peso normal"
    elif calculo_imc >= 25 and calculo_imc <= 29.9:
        lbl_resultado["text"] = f"Seu nome é {nome} e seu IMC: {calculo_imc:.2f} - Sobrepeso"
    else:
        lbl_resultado["text"] = f"Seu nome é {nome} e seu IMC: {calculo_imc:.2f} - Obesidade"


# 1. Criar a janela
janela = tk.Tk()
# 1.2 Configurar a janela
janela.title("Boas vindas ao  sistema")
janela.geometry("300x400")
janela.resizable(False, False)

#2. Adicionar elementos(widgets)
lbl_titulo = Label(janela, text="Calculo de IMC", pady=15).pack()
lbl_nome = Label(janela, text="Nome").pack()
txt_nome = Entry(janela)
txt_nome.pack()

lbl_peso = Label(janela, text="Peso").pack()
txt_peso = Entry(janela)
txt_peso.pack()

lbl_altura = Label(janela, text="Altura (cm)").pack()
txt_altura = Entry(janela)
txt_altura.pack()

btn_calcular = Button(janela, text="Calcular", command=mostrar_mensagem)
btn_calcular.pack()

lbl_resultado = Label(janela, pady=20)
lbl_resultado.pack()

#3. Mostrar a janela
janela.mainloop()