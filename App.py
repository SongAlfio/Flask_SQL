from flask import Flask, render_template, send_file, make_response, url_for, Response,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return render_template("Esercizio1/Search.html")

@app.route('/result', methods=['GET'])
def result():
  # Collegamento al database
  import pandas as pd 
  import pymssql
  conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')  
  # Invio Query al database e ricezione informazioni
  Nome_Prodotto = request.args['NomeProdotto']
  query = f"Select * from Production.Products inner join Production.Categories on Production.Categories.Category_ID = Production.Products.Category_ID inner join Production.Brands on Production.Brands.Brand_ID = Production.Products.Brand_ID where product_name like '{Nome_Prodotto}%'"
  df_Prodotti = pd.read_sql(query,conn)
  # Visualizzare le informazione.
  df_Prodotti
  return render_template('Esercizio1/result.html', nomiColonne = df_Prodotti.columns.values, dati = list(df_Prodotti.values.tolist()))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)