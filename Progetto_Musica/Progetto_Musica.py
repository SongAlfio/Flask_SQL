from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)
import pandas as pd 
import pymssql

@app.route('/', methods=['GET'])
def home():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')  

    query = 'Select Category_Name, Count(*) as Numero_Prodotti from Production.Products inner join Production.Categories on Production.Categories.Category_id = Production.Products.Category_id group by Production.Products.Category_id,Production.Categories.Category_name order by Numero_Prodotti desc'
    df = pd.read_sql(query,conn)
    names = list(df['Category_Name'])
    values = list(df['Numero_Prodotti'])
    fig1 = plt.figure(figsize=[16,16])
    ax = plt.axes()
    ax.bar(names, values)
    fig1.autofmt_xdate(rotation=45) 
    fig1.suptitle('Categorie di ogni prodotto', color='k')
    plt.savefig('static/images/plot.png')
    
    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)