from tkinter import Tk, ttk
from tkinter import *
from PIL import ImageTk, ImageOps, ImageDraw
import requests
import json
import string
#Importando bibliotecas


#cores

cor0 = "#FFFFFF"
cor1 = '#333333'
cor2 = '#38576b'

#Configurando a janela
janela = Tk()
janela.geometry('400x420')
janela.title('Conversor de Moedas')
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#Divisao da janela

frame_cima = Frame(janela, width=400, height=70, padx=0, pady=0, bg=cor2, relief='flat')
frame_cima.grid(row=0, column= 0, columnspan=2)


frame_baixo = Frame(janela, width=400, height=270, padx=0, pady=5, bg=cor0, relief='flat')
frame_baixo.grid(row=1, column= 0, sticky=NSEW)

#função converter 
def converter():
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_recebido = valor.get()
    response = requests.get("https://api.exchangerate-api.com/v4/latest/{}".format(moeda_de))
    dados = json.loads(response.text)

    cambio =(dados['rates'][moeda_para])

    resultado = float(valor_recebido)* float(cambio)

    if moeda_para == 'USD':
        simbolo = '$'
    elif moeda_para == 'EUR':
        simbolo = '€'
    elif moeda_para == 'INR':
        simbolo = '₹'
    elif moeda_para == 'AOA':
        simbolo = 'Kz'
    elif moeda_para == 'ALL':
        simbolo = 'L'
    elif moeda_para == 'SAR':
        simbolo = 'ر.س'
    elif moeda_para == 'BDT':
        simbolo = '৳'
    elif moeda_para == 'XAF':
        simbolo = 'Fr'
    else:
        simbolo = 'R$'   

    moeda_equivalente = simbolo + "{:,.2f}".format(resultado) 
    app_resultado['text'] = moeda_equivalente



app_nome = Label(frame_cima, compound=CENTER, text='Conversor de moeda', height=5, padx=13, pady=30, relief='flat', anchor=NW, font=("Arial 18 bold"), bg=cor2, fg=cor0)
app_nome.place(x=72, y=1)

app_resultado = Label(frame_baixo, compound=LEFT, text='', width=16, height=2, relief='solid', anchor=CENTER, font=("Ivy 16 bold"), bg=cor0, fg=cor1)
app_resultado.place(x=100, y=10)



moeda = ['AOA', 'BRL','EUR', 'INR', 'USD', 'XAF', 'BDT', 'SAR', 'ALL']



app_de = Label(frame_baixo, compound=LEFT, text='De', width=18, height=1, relief='flat', anchor=NW, font=("Ivy 10 bold"), bg=cor0, fg=cor1)
app_de.place(x=100, y=90)
combo_de = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo_de.place(x=100, y=115)
combo_de['values']= (moeda)


app_para = Label(frame_baixo, compound=LEFT, text='Para', width=18, height=1, relief='flat', anchor=NW, font=("Ivy 10 bold"), bg=cor0, fg=cor1)
app_para.place(x=220, y=90)
combo_para = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo_para.place(x=220, y=115)
combo_para['values']= (moeda)

valor = Entry(frame_baixo, width=23, justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=100, y=155)

botao = Button(frame_baixo, command=converter, text='Converter', width=17, padx=19, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), relief='raised', overrelief=RIDGE)
botao.place(x=100, y=190)

def limpar():
    combo_de.set('')  # Define a primeira caixa de seleção como vazia
    combo_para.set('')  # Define a segunda caixa de seleção como vazia
    valor.delete(0, END)  # Limpa o campo de entrada
    app_resultado['text'] = ''  # Limpa o rótulo de resultado

# Botão para limpar
botao_limpar = Button(frame_baixo, text='Limpar', command=limpar, width=17, padx=19, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), relief='raised', overrelief=RIDGE)
botao_limpar.place(x=100, y=230)



janela.mainloop()