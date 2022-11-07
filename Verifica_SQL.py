#Realizzare un sito web cyhe permetta di visualizzare tutti i dipendenti che lavorano in un certo store. 
#Il maneger inserisce il nome dello store e clicca su un bottone che invia i dati al server. 
#Quest'ultimo accede al database e restituisce i nomi e i cognomi dei dipendenti di quello store. 
#Se il nome dello store non è presente, deve essere restituito un opportuno messaggio di errore. 
#Tutta la parte grafica deve essere gestita con Bootstrap.

from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)
import pandas as pd 
import pymssql

@app.route('/', methods=['GET'])
def home():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')  
    query = "Select * from Sales.stores "
    df_Store = pd.read_sql(query,conn)
    df_Store
    return render_template("Verifica_SQL/Home.html", nomiColonne = df_Store.columns.values, dati = list(df_Store.values.tolist()))

@app.route('/Risultato', methods=['GET'])
def Risultato():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio') 
    Nome_Store = request.args['NomeStore']

    query = f"Select first_name, last_name from Sales.staffs inner join sales.stores on sales.stores.store_id = sales.staffs.store_id where store_name = '{Nome_Store}'"
    df = pd.read_sql(query,conn)
    df
    
    if df.values.tolist() != []:
        return render_template("Verifica_SQL/Risultato.html", nomiColonne = df.columns.values, dati = list(df.values.tolist()))
    else:
        return render_template("Verifica_SQL/Errore.html", Nome_Errore = Nome_Store)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)