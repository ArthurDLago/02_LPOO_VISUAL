import tkinter as tk
from tkinter import Label, Entry, Button, messagebox


class Pessoa:
    def __init__(self, nome: str, peso: float, altura_cm: float) -> None:
        self._nome = nome
        self._peso = peso
        self._altura_cm = altura_cm

    def calcular_imc(self) -> float:
        altura_m = self._altura_cm / 100
        return self._peso / (altura_m * altura_m)

    def mostrar_info(self) -> str:
        imc = self.calcular_imc()
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc <= 24.9:
            classificacao = "Peso normal"
        elif imc <= 29.9:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"
        return f"Seu nome é {self._nome} e seu IMC: {imc:.2f} - {classificacao}"


def calcular_imc():
    nome = txt_nome.get()
    try:
        peso = float(txt_peso.get())
        altura_cm = float(txt_altura.get())
        pessoa = Pessoa(nome, peso, altura_cm)

        janela_resultado = tk.Toplevel(janela)
        janela_resultado.title("Resultado do IMC")
        janela_resultado.geometry("280x200")
        janela_resultado.resizable(False, False)

        info_texto = pessoa.mostrar_info()

        lbl_nome_res = Label(janela_resultado, text=f"Nome: {nome}")
        lbl_nome_res.pack(pady=5)

        lbl_peso_res = Label(janela_resultado, text=f"Peso: {peso:.2f} kg")
        lbl_peso_res.pack(pady=5)

        lbl_altura_res = Label(janela_resultado, text=f"Altura: {altura_cm:.1f} cm")
        lbl_altura_res.pack(pady=5)

        lbl_grau_res = Label(janela_resultado, text=info_texto)
        lbl_grau_res.pack(pady=10)

        btn_fechar = Button(janela_resultado, text="Fechar", command=janela_resultado.destroy)
        btn_fechar.pack(pady=5)

    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos para peso e altura.")


janela = tk.Tk()
janela.title("Boas vindas ao sistema")
janela.geometry("300x400")
janela.resizable(False, False)

lbl_titulo = Label(janela, text="Cálculo de IMC", pady=15)
lbl_titulo.pack()

lbl_nome = Label(janela, text="Nome")
lbl_nome.pack()
txt_nome = Entry(janela)
txt_nome.pack()

lbl_peso = Label(janela, text="Peso (kg)")
lbl_peso.pack()
txt_peso = Entry(janela)
txt_peso.pack()

lbl_altura = Label(janela, text="Altura (cm)")
lbl_altura.pack()
txt_altura = Entry(janela)
txt_altura.pack()

btn_mostrar = Button(janela, text="Mostrar resultado", command=calcular_imc)
btn_mostrar.pack(pady=20)

janela.mainloop()