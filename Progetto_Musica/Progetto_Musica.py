from flask import Flask, request, jsonify
import pandas as pd
import pymssql as sql
from flask_cors import CORS

from os import getenv
from dotenv import load_dotenv
load_dotenv()

db_server = getenv("DB_SERVER")
db_user = getenv("DB_USER")
db_password = getenv("DB_PASSWORD")
db_name = getenv("DB_NAME")

conn = sql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    
    return jsonify(res)

@app.route('/Sign_Up', methods=['GET'])
def Sign_Up():
    Nome_utente = request.args['Nome_utente']
    Email = request.args['Email']
    Password = request.args['Password']
    Età = request.args['Età']
    Sesso = request.args['Sesso']
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')  
    query=f"insert into utente(Nick_Name, email, password, Età, Sesso) values(‘{Nome_utente}’, ‘{Email}’,’{Password}’,’{Età}’,’{Sesso}’)"    
    df = pd.read_sql(query,conn)
    
    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)