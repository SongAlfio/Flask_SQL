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

#1. Registrazione
@app.route('/Sign_Up', methods=['GET'])
def Sign_Up():
    Nome_utente = request.args['Nome_utente']
    Email = request.args['Email']
    Password = request.args['Password']
    Età = request.args['Età']
    Sesso = request.args['Sesso']
    query=f"insert into Musica.Utente(Nick_Name, Email, Password, Età, Sesso) values('{Nome_utente}', '{Email}','{Password}','{Età}','{Sesso}')"    
    df = pd.read_sql(query,conn)
    
    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')

#2. Login
@app.route('/Login', methods=['GET'])
def Login():
    Nome_utente = request.args['Nome_utente']
    Email = request.args['Email']
    Password = request.args['Password']
    query= f"select * from Musica.Login where Nome_utente='{Nome_utente}' and Email='{Email}' and Password='{Password}'"

    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')

#3. Modifica Informazioni Utente
@app.route('/Modifica_Nome', methods=['GET'])
def Modifica_Nome():
    New_name = request.args['New_name']
    Email = request.args['Email']
    Password = request.args['Password']
    query=f"update Musica.Utente set Nome_utente = '{New_name}' where Email='{Email}' and Password='{Password}'"

    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')

@app.route('/Modifica_Email', methods=['GET'])
def Modifica_Email():
    New_Email = request.args['New_Email']
    Email = request.args['Email']
    Password = request.args['Password']
    query=f"update Musica.Utente set Email= '{New_Email}' where where Email='{Email}' and Password='{Password}'"

    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')

@app.route('/Modifica_Pass', methods=['GET'])
def Modifica_Pass():
    New_Pass = request.args['New_Pass']
    Old_Email = request.args['Email']
    query=f"update Musica.Utente set Password= '{New_Password}' where Email='{Old_Email}'"

    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')

#4. Visualizzazione info utente
@app.route('/Info_Utente', methods=['GET'])
def Info_Utente():
    Nome_utente = request.args['Nome_utente']
    Email = request.args['Email']
    Password = request.args['Password']
    query=f"delete from Musica.Utente where Nome_utente='{Nome_Utente}' and Email='{Email}' and Password ='{Password}'"
    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')

#5. Rimozione account:
@app.route('/Delete_Account', methods=['GET'])
def Delete_Account():
    New_Pass = request.args['New_Pass']
    Old_Email = request.args['Email']
    query=f"select Nome_Utente, Email, Password from Musica.Utente  where Email='{Email}' and Password='{Password}'"

    return render_template('Progetto_Musica/Home.html', url='/static/images/plot.png',url1='/static/images/plot1.png', url2='/static/images/plot2.png')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)