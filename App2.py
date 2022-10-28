# Analizzare un sito web che permette all'utente di visualizzare una serie di informazioni riguardanti alla società bikestore. da homepage del sito si permette all'utente di scegliere una fra le seguenti 3 opzioni: 
# 1. Il numero di prodotti per ogni categoria, sia In formato tabellare, sia sotto forma di grafico a barre verticale
# 2. Il numero di ordini per ogni store, sia in sotto formato tabellare, sia sotto forma di grafico a barre orizzontali
# 3. Numero di prodotti per ogni brand, sia in formato tabellare, sia sotto forma di gragico a torta
# 4. L'elenco dei prodotti che iniziano con una certa stringa di carattere.
# Una volta effettuato la scelta l'utente clicca su un bottone che fornisce le informazione richieste.
# Utilizzare bootstrap per la parte pratica.
from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd 
import pymssql
import io

@app.route('/', methods=['GET'])
def home():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')  

    query = 'Select Category_Name, Count(*) as Numero_Prodotti from Production.Products inner join Production.Categories on Production.Categories.Category_id = Production.Products.Category_id group by Production.Products.Category_id,Production.Categories.Category_name order by Numero_Prodotti desc'
    df = pd.read_sql(query,conn)
    names = list(df['Category_Name'])
    values = list(df['Numero_Prodotti'])
    fig1 = plt.figure(figsize=[15,15])
    ax = plt.axes()
    ax.bar(names, values)
    fig1.autofmt_xdate(rotation=45) 
    plt.savefig('static/images/plot.png')

    query1 = 'Select Store_Name, Count(*) as Numero_Ordini from Sales.Stores inner join Sales.Orders on Sales.Stores.Store_id = Sales.Orders.Store_id group by Sales.Orders.Store_id,Sales.Stores.Store_name order by Numero_Ordini desc'
    df1 = pd.read_sql(query1,conn)
    names = list(df1['Store_Name'])
    values = list(df1['Numero_Ordini'])
    fig2 = plt.figure(figsize=[15,15])
    ax = plt.axes()
    ax.barh(names, values)
    fig2.autofmt_xdate(rotation=0) 
    plt.yticks(rotation = 45)
    plt.savefig('static/images/plot1.png')
    
    query2 = 'Select Brand_Name, Count(*) as Numero_Prodotti from Production.Products inner join Production.Brands on Production.Brands.Brand_id = Production.Products.Brand_id group by Production.Products.Brand_id,Production.Brands.Brand_name order by Numero_Prodotti desc'
    df2 = pd.read_sql(query2,conn)
    names = list(df2['Brand_Name'])
    values = list(df2['Numero_Prodotti'])
    plt.rcParams.update({'font.size': 20})    # Aumenta la grandezza del testo (Default: 10)
    fig3 = plt.figure(figsize=[15,15])
    ax = plt.axes()
    ax.pie(values, labels=names, startangle=90, autopct='%1.1f%%')#grafico a torta
    
    fig3.suptitle('Numeri prodotti per ogni brand', color='k')
    plt.savefig('static/images/plot2.png')
    
    return render_template('Esercizio2/Cerca.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')

@app.route('/Cerca', methods=['GET'])
def Cerca():
  global Cerca
  Cerca = request.args['Cerca']
  if Cerca == 'NomeProdotto':
    return render_template('Esercizio2/Search_Name.html')
  if Cerca == 'NomeCategoty':
    return render_template('Esercizio2/Search_Category.html', url='/static/images/plot.png')
  if Cerca == 'NomeNegozio':
    return render_template('Esercizio2/Search_Negozio.html', url1='/static/images/plot1.png')
  if Cerca == 'NomeBrand':
    return render_template('Esercizio2/Search_Brand.html', url2='/static/images/plot2.png')

  return render_template('Esercizio2/Cerca.html')

@app.route('/result_Name', methods=['GET'])
def result_Name():
  # Collegamento al database
  
  conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')  
  # Invio Query al database e ricezione informazioni
  Nome_Prodotto = request.args['NomeProdotto']
  query = f"Select * from Production.Products inner join Production.Categories on Production.Categories.Category_ID = Production.Products.Category_ID inner join Production.Brands on Production.Brands.Brand_ID = Production.Products.Brand_ID where product_name like '{Nome_Prodotto}%'"
  df_Prodotti = pd.read_sql(query,conn)
  # Visualizzare le informazione.
  df_Prodotti
  return render_template('Esercizio2/result_Name.html', nomiColonne = df_Prodotti.columns.values, dati = list(df_Prodotti.values.tolist()))

@app.route('/result_Category', methods=['GET'])
def result_Category():
  # Collegamento al database
  
  conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')  
  # Invio Query al database e ricezione informazioni
  Nome_Category = request.args['NomeCategory']
  query = f"Select * from Production.Products inner join Production.Categories on Production.Categories.Category_ID = Production.Products.Category_ID inner join Production.Brands on Production.Brands.Brand_ID = Production.Products.Brand_ID where Category_name like '{Nome_Category}%'"
  df_Prodotti = pd.read_sql(query,conn)
  # Visualizzare le informazione.
  df_Prodotti
  return render_template('Esercizio2/result_Category.html', nomiColonne = df_Prodotti.columns.values, dati = list(df_Prodotti.values.tolist()))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)