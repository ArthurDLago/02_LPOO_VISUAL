import tkinter as tk
from tkinter import Label, Entry, Button, messagebox


def mostrar_mensagem():
    nome = txt_nome.get()
    if(nome.strip()):
        lbl_resultado['text'] = (f"Bem-vindo {nome}")
        txt_nome.delete(0, tk.END)
        messagebox.showinfo("Acesso ao sistema", f"Bem-vindo {nome}")
    else:
        messagebox.showerror("Aviso", "Por favor, digite seu nome")
# 1. Criar a janela
janela = tk.Tk()
# 1.2 Configurar a janela
janela.title("Boas vindas ao  sistema")
janela.geometry("300x400")
janela.resizable(False, False)

#2. Adicionar elementos(widgets)
lbl_titulo = Label(janela, text="Cadastro de Usuario", pady=15).pack()
lbl_nome = Label(janela, text="Nome").pack()
txt_nome = Entry(janela)
txt_nome.pack()

btn_salvar = Button(janela, text="Salvar", command=mostrar_mensagem)
btn_salvar.pack()

lbl_resultado = Label(janela, pady=20)
lbl_resultado.pack()

#3. Mostrar a janela
janela.mainloop()