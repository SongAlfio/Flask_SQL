#Realizzare un sito web che permetta di visualizzare le informazioni riguardanti i clienti.
#Un componente dello staff richiama la rotta /infoUser dove sono presenti due text per l'inserimento del nome e del cognome del cliente ed un bottone per inviare le informazioni, 
#Una volta inviate, il sito risponde con tutte le informazioni relative a quel cliente, una sotto l'altra. 
#Se il cliente non esiste, deve essere visualizzato un opportuno messaggio di errore. 
#Utilizzare Bootstrap per l'interfaccia grafica di tutte le pagine.


from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)
import pandas as pd 
import pymssql

@app.route('/InfoUser', methods=['GET'])
def InfoUser():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio') 

    df_Utente = pd.read_sql(query,conn)

    return render_template("Verifica_SQL2/InfoUser.html", nomiColonne = df_Utente.columns.values, dati = list(df_Utente.values.tolist()))

@app.route('/Risultato', methods=['GET'])
def Risultato():
    Nome_Utente = request.args['Nome_Utente']
    Cognome_Utente = request.args['Cognome_Utente']
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio') 
    query = f"Select * from Sales.Customers where first_name = '{Nome_Utente}' and last_name = '{Cognome_Utente}'"
    df_Utente = pd.read_sql(query,conn)
    df_Utente
    if df_Utente.values.tolist() == []:
        return render_template("Verifica_SQL2/Errore.html")
    else:
        return render_template("Verifica_SQL2/Risultato.html", nomiColonne = df_Utente.columns.values, dati = list(df_Utente.values.tolist()))




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)