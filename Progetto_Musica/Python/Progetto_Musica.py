from flask import Flask, render_template, send_file, request, make_response, redirect, url_for, Response, redirect, jsonify
import pandas as pd
import pymssql as sql
from flask_cors import CORS
from os import getenv
from dotenv import load_dotenv

load_dotenv()


conn = sql.connect(server='213.140.22.237\SQLEXPRESS', user='song.alfio', password='xxx123##', database='song.alfio')

app = Flask(__name__)
CORS(app)
#0. Home Page
@app.route('/', methods=['GET'])
def Home():
  return render_template("Home.html")

@app.route('/2', methods=['GET'])
def Home2():
  return render_template("Home2.html")

#1. Registrazione
@app.route('/Sign_Up', methods=['GET'])
def Sign_Up():    
    return render_template("Sign_Up.html")

@app.route('/Registrazione', methods=['POST'])
def Registrazione():    

    Nome_utente = request.args['Nome_utente']
    Email = request.args['Email']
    Password = request.args['Password']
    Età = request.args['Età']
    Sesso = request.args['Sesso']

    cursor = conn.cursor()
    query = f"insert into Musica.Utente(Nick_Name, Email, Password, Età, Sesso) values('{Nome_utente}', '{Email}','{Password}','{Età}','{Sesso}')"
    
    cursor.execute(query)
    conn.commit()

    return render_template("Home.html")
    

#2. Login
@app.route('/Login_Page', methods=['GET'])
def Login_Page():    
    return render_template("Login.html")

@app.route('/Login', methods=['POST'])
def Login():
    U_O_E = request.args['U_O_E']
    Password = request.args['Password']
    query= f"select * from Musica.Utente where Nick_Name='{U_O_E}' or Email='{U_O_E}' and Password='{Password}'"
    df2 = pd.read_sql(query, conn)

    return jsonify(list(df2.to_dict('index').values()))

#3. Modifica Informazioni Utente
@app.route('/Modifica_Nome', methods=['GET'])
def Modifica_Nome():
    New_name = request.args['New_name']
    Email = request.args['Email']
    Password = request.args['Password']
    query=f"update Musica.Utente set Nick_Name = '{New_name}' where Email='{Email}' and Password='{Password}'"
    df3 = pd.read_sql(query,conn)

    return jsonify(list(df3.to_dict('index').values()))

@app.route('/Modifica_Email', methods=['GET'])
def Modifica_Email():
    New_Email = request.args['New_Email']
    Email = request.args['Email']
    Password = request.args['Password']
    query=f"update Musica.Utente set Email= '{New_Email}' where where Email='{Email}' and Password='{Password}'"
    df3_1 = pd.read_sql(query,conn)

    return jsonify(list(df3_1.to_dict('index').values()))

@app.route('/Modifica_Pass', methods=['GET'])
def Modifica_Pass():
    New_Pass = request.args['New_Pass']
    Old_Email = request.args['Email']
    query=f"update Musica.Utente set Password= '{New_Password}' where Email='{Old_Email}'"
    df3_2 = pd.read_sql(query,conn)

    return jsonify(list(df3_2.to_dict('index').values()))

#4. Visualizzazione info utente
@app.route('/Info_Utente', methods=['GET'])
def Info_Utente():
    Nome_utente = request.args['Nome_utente']
    Email = request.args['Email']
    Password = request.args['Password']
    query=f"delete from Musica.Utente where Nick_Name='{Nome_Utente}' and Email='{Email}' and Password ='{Password}'"
    df4 = pd.read_sql(query,conn)

    return jsonify(list(df4.to_dict('index').values()))

#5. Rimozione account:
@app.route('/Delete_Account', methods=['GET'])
def Delete_Account():
    New_Pass = request.args['New_Pass']
    Old_Email = request.args['Email']
    query=f"select Nick_Name, Email, Password from Musica.Utente  where Email='{Email}' and Password='{Password}'"
    df5 = pd.read_sql(query,conn)

    return jsonify(list(df5.to_dict('index').values()))

#6. Search
@app.route('/Search', methods=['GET'])
def Search():
    Search = request.args['Search']
    query=f"select Nick_Name, Musica.Canzone.Nome from Musica.Utente inner join Musica.Ascolta on Musica.Utente.id = Musica.Ascolta.ID_Utente inner join Musica.Canzone on Musica.Canzone.id = Musica.Ascolta.ID_Canzone where Nick_Name = '{Search}'"
    df6 = pd.read_sql(query,conn)

    return jsonify(list(df6.to_dict('index').values()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)