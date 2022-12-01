from tkinter import *
from tkinter import ttk

#cores usadas nesse projeto

cor1 = "#000000"  #preto
cor2 = "#1e4a29"  #verde escuro
cor3 = "#b0b5b1"  #cinza
cor4 = "#b31414"  #vermelho
cor5 = "#f7f5f5"  #branco



#criando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)


#Criando a tela da calculadora
frame_display = Frame(janela, width=235, height=50, bg= cor2)
frame_display.grid(row=0, column=0)


#criando corpo do teclado 
frame_corpo = Frame(janela, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)


#label
valor_texto = StringVar()
app_tela = Label(frame_display, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg=cor2, fg=cor5)
app_tela.place(x=0, y=0)


#variavel global para as teclas
todos_os_valores = ''

#criando as funções
def entra_valores(valor_digitado):
    global todos_os_valores

    todos_os_valores = todos_os_valores + str(valor_digitado)

    #passar valor para a tela
    valor_texto.set(todos_os_valores)

def calcula_valores():
    global todos_os_valores
    resultado = eval(todos_os_valores)
    valor_texto.set(resultado)

#função para limpar a tela
def limpa_tela():
    global todos_os_valores
    todos_os_valores = ""
    valor_texto.set("")



#criando botões relief = estilo do botão ao ser clicado overrelief = estilo do botão ao passar o mouse por cima

#botão Clean (C)
botao_clean = Button(frame_corpo, text="C", width=11, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= limpa_tela)
botao_clean.place(x=0, y=0)

#botão de porcentagem (%)
botao_porcentagem = Button(frame_corpo, text="%", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('%'))
botao_porcentagem.place(x=119, y=0)

#Botão de divisão (/) fg=cor do texto
botao_divisao = Button(frame_corpo, text="/", width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('/'))
botao_divisao.place(x=177, y=0)

#botão de multiplicação (*)
botao_multiplicacao = Button(frame_corpo, text="*", width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('*'))
botao_multiplicacao.place(x=177, y=54)

#botão de subtrair (-)
botao_subtracao = Button(frame_corpo, text="-", width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('-'))
botao_subtracao.place(x=177, y=108)

#botão de somar (+)
botao_subtracao = Button(frame_corpo, text="+", width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('+'))
botao_subtracao.place(x=177, y=162)

#botão ponto (.)
botao_ponto = Button(frame_corpo, text=".", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('.'))
botao_ponto.place(x=119, y=216)

#botão de resultado (=)
botao_subtracao = Button(frame_corpo, text="=", width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= calcula_valores)
botao_subtracao.place(x=177, y=216)


#teclado numeral
botao_numero_7 = Button(frame_corpo, text="7", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('7'))
botao_numero_7.place(x=0, y=54,)
botao_numero_8 = Button(frame_corpo, text="8", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('8'))
botao_numero_8.place(x=59, y=54)
botao_numero_9 = Button(frame_corpo, text="9", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('9'))
botao_numero_9.place(x=119, y=54)

botao_numero_4 = Button(frame_corpo, text="4", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('4'))
botao_numero_4.place(x=0, y=108)
botao_numero_5 = Button(frame_corpo, text="5", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('5'))
botao_numero_5.place(x=59, y=108)
botao_numero_6 = Button(frame_corpo, text="6", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('6'))
botao_numero_6.place(x=119, y=108)

botao_numero_1 = Button(frame_corpo, text="1", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('1'))
botao_numero_1.place(x=0, y=162)
botao_numero_2 = Button(frame_corpo, text="2", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('2'))
botao_numero_2.place(x=59, y=162)
botao_numero_3 = Button(frame_corpo, text="3", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('3'))
botao_numero_3.place(x=119, y=162)

botao_numero_0 = Button(frame_corpo, text="0", width=11, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entra_valores('0'))
botao_numero_0.place(x=0, y=216)


janela.mainloop()