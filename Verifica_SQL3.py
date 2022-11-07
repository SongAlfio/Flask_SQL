#Realizzare un sito web che permetta di visualizzare l'elenco dei primi 10 clienti che hanno speso di più. 
#Il maneger di BikeStore si collega alla rotta /bestCustomers e riceve l'elenco dei clienti. 
#Cliccando poi sull'ID di uno dei clienti, si deve poter visualizzare l'elenco degli ordini effettuati. 
#Utilizzare Bootstrap per l'interfaccia grafica.


from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)
import pandas as pd 
import pymssql

@app.route('/bestCustomers', methods=['GET'])
def bestCustomers():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio') 
    query = f"Select TOP 10 first_name, last_name from (select * from Sales.Customers inner join sales.orders on Sales.Customers.Customer_id = sales.orders.Customer_ID inner join Sales.order_Item on Sales.order_Item.Order_id = sales.orders.Order_id group by Customer_ID order by list_price desc) inner join sales.orders on Sales.Customers.Customer_id = sales.orders.Customer_ID inner join Sales.order_Item on Sales.order_Item.Order_id = sales.orders.Order_id"
    df_Utente = pd.read_sql(query,conn)
    return render_template("Verifica_SQL3/bestCustomers.html", nomiColonne = df_Utente.columns.values, dati = list(df_Utente.values.tolist()))





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)