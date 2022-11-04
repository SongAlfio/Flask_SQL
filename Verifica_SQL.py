from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)
import pandas as pd 
import pymssql
import io

@app.route('/', methods=['GET'])
def home():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')  
    query = f"Select * from Sales.stores "
    df_Store = pd.read_sql(query,conn)
    df_Store
    return render_template("Verifica_SQL/Home.html", nomiColonne = df_Store.columns.values, dati = list(df_Store.values.tolist()))

@app.route('/Risultato', methods=['GET'])
def Risultato():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio') 
    Nome_Store = request.args['NomeStore']

    query = f"Select first_name, last_name from Sales.staffs inner join sales.stores on sales.stores.store_id = sales.staffs.store_id where store_name like '{Nome_Store}%'"
    df = pd.read_sql(query,conn)
    df
    query = f"select store_name from Sales.stores"
    df1 = pd.read_sql(query,conn)
    df1
    List_df1 = df1[df1['store_name'].str.contains(Nome_Store)]['store_name'].to_list()
    if len(List_df1) != 0:
        return render_template("Verifica_SQL/Risultato.html", nomiColonne = df.columns.values, dati = list(df.values.tolist()))
    else:
        return render_template("Verifica_SQL/Errore.html", Nome_Errore = Nome_Store)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)