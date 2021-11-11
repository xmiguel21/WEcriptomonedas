from bs4 import BeautifulSoup
import requests
import  pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas_datareader as pdr
from datetime import datetime, timedelta
import mplfinance as mpf
from PIL import Image, ImageTk
from threading import Thread

url = 'https://coinmarketcap.com/es/'
page = requests.get(url)
cont = page.text

listaMonedas = []

soup = BeautifulSoup(cont, 'lxml')

box = soup.find('html' , lang = 'es')

tex = box.find('h1', class_ = 'sc-1q9q90x-0 TyVlS')
titulo= tex.get_text()

#priemr a moneda
lista_paginas = ['https://coinmarketcap.com/es/currencies/bitcoin/',
 'https://coinmarketcap.com/es/currencies/ethereum/',
 'https://coinmarketcap.com/es/currencies/binance-coin/',
'https://coinmarketcap.com/es/currencies/cardano/',
'https://coinmarketcap.com/es/currencies/tether/' ]

for x in range(5):

    url=lista_paginas[x]

    page1 = requests.get(url)
    cont1 = page1.text

    soup2 = BeautifulSoup(cont1, 'lxml')

    v = soup2.find('div' , class_= 'sc-16r8icm-0 kjciSH priceSection')
    moneda = soup2.find('small', class_='nameSymbol').get_text()
    valor = v.find('div' , class_ = 'sc-16r8icm-0 kjciSH priceTitle').get_text()
    minimo = v.find('span' , class_ = 'n78udj-5 dBJPYV').get_text()
    x = soup2.find('div' , class_= 'sc-16r8icm-0 SjVBR')
    maximo = x.find('span' , class_ = 'n78udj-5 dBJPYV').get_text()
    a = soup2.find('div', class_='sc-16r8icm-0 fggtJu statsSection')
    con = 0

    # obtencion del volumen capital de la moneda

    for volu in a.findAll('div', class_='statsBlock'):
        if con == 2:
            for q in volu:
                if con == 3:
                    volumen = q.find('div', class_='statsValue').get_text()
                    print('voulumen de moneda: ' +str(volumen))
                con = con+1
        con= con+1


    tex2 = soup2.find('h2', class_='sc-1q9q90x-0 jCInrl h1')
    titulo2 = tex2.get_text()

    # grafico de velas
    # int_date = datetime.now() - timedelta(days=30)
    # info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    # mpf.plot(info, type='candle', title='valor '+ titulo2, style='charles')
    listaMonedas.append(titulo2)
    listaMonedas.append(valor)
    listaMonedas.append(minimo)
    listaMonedas.append(maximo)

def graficoBitcoin():

    # procedimiento de scrapping solo para bitcoin
    url = 'https://coinmarketcap.com/es/currencies/bitcoin/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Bitcoin', style='charles')

def frameBitcoin():
    top = Toplevel()
    top.title("Bitcoin")
    top.geometry("800x600")
    header = Frame(top, width=1200, height=180, bg="white")
    header.pack()
    body = Frame(top, width=1200, height=480, bg="#E5F3F7")
    body.pack()

    img = Image.open('images_coins/1.png')
    img = ImageTk.PhotoImage(img)
    img_label = Label(top, image=img, bg="white")
    img_label.Image = img
    img_label.place(x=20, y=16)

    name = Label(top, text=listaMonedas[0], bg="white", font=("Aharoni", 25, 'bold'))
    name.place(x=200, y=75)

    value = Label(top, text=listaMonedas[1], bg="white", font=("Aharoni", 25, 'bold'))
    value.place(x=500, y=75)

    top.mainloop()


def graficoEtherium():
    # procedimiento de scrapping solo para etherium
    url = 'https://coinmarketcap.com/es/currencies/ethereum/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Etherium', style='charles')

def frameEtherium():
    top = Toplevel()
    top.title("Etherium")
    top.geometry("800x600")
    header = Frame(top, width=1200, height=180, bg="white")
    header.pack()
    body = Frame(top, width=1200, height=480, bg="#E5F3F7")
    body.pack()

    img = Image.open('images_coins/2.png')
    img = ImageTk.PhotoImage(img)
    img_label = Label(top, image=img, bg="white")
    img_label.Image = img
    img_label.place(x=20, y=16)

    name = Label(top, text=listaMonedas[4], bg="white", font=("Aharoni", 25, 'bold'))
    name.place(x=200, y=75)

    value = Label(top, text=listaMonedas[5], bg="white", font=("Aharoni", 25, 'bold'))
    value.place(x=500, y=75)

def graficoBinance():
    # procedimiento de scrapping solo para binance
    url = 'https://coinmarketcap.com/es/currencies/binance-coin/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Binance', style='charles')

def frameBinance():
    top = Toplevel()
    top.title("Binance")
    top.geometry("800x600")
    header = Frame(top, width=1200, height=180, bg="white")
    header.pack()
    body = Frame(top, width=1200, height=480, bg="#E5F3F7")
    body.pack()

    img = Image.open('images_coins/3.png')
    img = ImageTk.PhotoImage(img)
    img_label = Label(top, image=img, bg="white")
    img_label.Image = img
    img_label.place(x=20, y=16)

    name = Label(top, text=listaMonedas[8], bg="white", font=("Aharoni", 25, 'bold'))
    name.place(x=200, y=75)

    value = Label(top, text=listaMonedas[9], bg="white", font=("Aharoni", 25, 'bold'))
    value.place(x=550, y=75)

def graficoCardano():
    # procedimiento de scrapping solo para cardano
    url = 'https://coinmarketcap.com/es/currencies/cardano/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Cardano', style='charles')

def frameCardano():
    top = Toplevel()
    top.title("Cardano")
    top.geometry("800x600")
    header = Frame(top, width=1200, height=180, bg="white")
    header.pack()
    body = Frame(top, width=1200, height=480, bg="#E5F3F7")
    body.pack()

    img = Image.open('images_coins/4.png')
    img = ImageTk.PhotoImage(img)
    img_label = Label(top, image=img, bg="white")
    img_label.Image = img
    img_label.place(x=20, y=16)

    name = Label(top, text=listaMonedas[12], bg="white", font=("Aharoni", 25, 'bold'))
    name.place(x=200, y=75)

    value = Label(top, text=listaMonedas[13], bg="white", font=("Aharoni", 25, 'bold'))
    value.place(x=500, y=75)

def graficotether():
    # procedimiento de scrapping solo para tether
    url = 'https://coinmarketcap.com/es/currencies/tether/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Tether', style='charles')

def frametether():
    top = Toplevel()
    top.title("Tether")
    top.geometry("800x600")
    header = Frame(top, width=1200, height=180, bg="white")
    header.pack()
    body = Frame(top, width=1200, height=480, bg="#E5F3F7")
    body.pack()

    img = Image.open('images_coins/5.png')
    img = ImageTk.PhotoImage(img)
    img_label = Label(top, image=img, bg="white")
    img_label.Image = img
    img_label.place(x=20, y=16)

    name = Label(top, text=listaMonedas[16], bg="white", font=("Aharoni", 25, 'bold'))
    name.place(x=200, y=75)

    value = Label(top, text=listaMonedas[17], bg="white", font=("Aharoni", 25, 'bold'))
    value.place(x=500, y=75)

def tabla():

    def item_selected(e):

        for selected_item in tablaTodos.selection():
            # dictionary
            item = tablaTodos.item(selected_item)
            # list
            valor = item['values'][0]

            nombreOpcion = item['text']
            imagen = item['image']
            abierto = item['open']

            if valor == 1:
                Thread(target=frameBitcoin()).start()
                Thread(target=graficoBitcoin()).start()
            elif valor == 2:
                Thread(target=graficoEtherium()).start()
                Thread(target=frameEtherium()).start()
            elif valor == 3:
                Thread(target=frameBinance()).start()
                Thread(target=graficoBinance()).start()
            elif valor == 4:
                Thread(target=frameCardano()).start()
                Thread(target=graficoCardano()).start()
            else:
                Thread(target=frametether()).start()
                Thread(target=graficotether()).start()


    # =======================
    #marcoTodos = LabelFrame(popup, text="Pacientes Con Alta Medica", bd=4, width=290, height=318, bg="#EDF0F2")
    #marcoTodos.place(x=50, y=30)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaTodos = ttk.Treeview(root, columns=(0, 1, 2,3,4), show='headings', height=14)
    tablaTodos.place(x=30, y=10)
    tablaTodos.tag_configure('oddrow', background="#26C1F4")
    tablaTodos.tag_configure('evenrow', background="#C0EAF8")
    tablaTodos.heading(0, text="N°")
    tablaTodos.heading(1, text="Nombre")
    tablaTodos.heading(2, text="valor")
    tablaTodos.heading(3, text="Precio Min 24h ")
    tablaTodos.heading(4, text="Precio Max 24h" )
    tablaTodos.column(0, width=10, minwidth=25)
    tablaTodos.column(1, width=120)
    tablaTodos.column(2, width=120)
    tablaTodos.column(3, width=120)
    tablaTodos.column(4, width=120)

    # agregando elementos
    tablaTodos.insert(parent='', index=1, iid=1,
                                  values=(1, listaMonedas[0] ,listaMonedas[1], listaMonedas[2], listaMonedas[3]),
                                  tags=('evenrow'))
    tablaTodos.insert(parent='', index=2, iid=2,
                      values=(2, listaMonedas[4], listaMonedas[5], listaMonedas[6], listaMonedas[7]),
                      tags=('oddrow'))
    tablaTodos.insert(parent='', index=3, iid=3,
                      values=(3, listaMonedas[8], listaMonedas[9], listaMonedas[10], listaMonedas[11]),
                      tags=('evenrow'))
    tablaTodos.insert(parent='', index=4, iid=4,
                      values=(4, listaMonedas[12], listaMonedas[13], listaMonedas[14], listaMonedas[15]),
                      tags=('oddrow'))
    tablaTodos.insert(parent='', index=5, iid=5,
                      values=(5, listaMonedas[16], listaMonedas[17], listaMonedas[18], listaMonedas[19]),
                      tags=('evenrow'))

    tablaTodos.bind('<Double-1>', item_selected)









root = Tk()
root.title("Scrapping Crypto")
root.geometry("600x500")
tabla()




root.mainloop()