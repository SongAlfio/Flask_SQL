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


#1. Registrazione
@app.route('/Sign_Up', methods=['GET'])
def Sign_Up():    
    return render_template("Sign_Up.html")

@app.route('/Registrazione', methods=['POST'])
def Registrazione():    

    Nome_utente = request.args['Nome_utente']
    Email = request.args['Email']
    Password = request.args['Password']
    Eta = request.args['Eta']
    Sesso = request.args['Sesso']

    cursor = conn.cursor()
    query = f"insert into Musica.Utente(Nick_Name, Email, Password, Eta, Sesso) values('{Nome_utente}', '{Email}','{Password}','{Eta}','{Sesso}')"
    
    cursor.execute(query)
    conn.commit()

    return conn
    

#2. Login
@app.route('/Login_Page', methods=['POST'])
def Login_Page():    
  email = request.args.get('email')
  print(email)
  password = request.args.get('password')
  print(password)

  data = {
    "statusCode": 200,
    "errorMessage": "",
    "data": {}
  }

  # Controllo se nono stati passati tutti i parametri richiesti
  if None not in [email, password]:
    # Prendo le informazioni dell'utente
    q = 'SELECT * FROM users WHERE email = %(e)s'
    cursor = conn.cursor(as_dict=True)
    cursor.execute(q, params={"e": email})
    res = cursor.fetchall()

    # Controllo se l'utente esiste
    if len(res) < 1:
      data["statusCode"] = 404
      data["errorMessage"] = "No user was found with that email"
    elif not (res[0]["password"] == password):
      data["statusCode"] = 403
      data["errorMessage"] = "Wrong password"
    else:
      data["data"] = res
  else:
    data['statusCode'] = 400
    data['errorMessage'] = "No email or password provided"
  
  return jsonify(data)

@app.route('/Login', methods=['GET','POST'])
def Login():
    U_O_E = request.form.get('U_O_E')
    Password = request.form.get('Password')
    query= f"select * from Musica.Utente where Nick_Name='{U_O_E}' or Email='{U_O_E}' and Password='{Password}'"
    
    if len(query) > 0 :
        df2 = pd.read_sql(query,conn)

        return redirect('http://127.0.0.1:4200/Home', Response=jsonify(list(df2.to_dict('index').values())))
    else:
        return Error


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
    query=f"Select * from Musica.Utente where Nick_Name='{Nome_Utente}' and Email='{Email}' and Password ='{Password}'"
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


@app.route('/Search2', methods=['GET'])
def Search2():
    query=f"select * from Musica.Canzone"
    df6_1 = pd.read_sql(query,conn)

    return jsonify(list(df6_1.to_dict('index').values()))

#7. Tutti i musicisti
@app.route('/Musicisti', methods=['GET'])
def Musicisti():
    query=f"select count(ID_Seguito) as Fans, Nick_Name, Sesso, Eta from Musica.Utente Full outer join Musica.Follow on Musica.Follow.ID_Follower = Musica.Utente.ID where Musica.Utente.ID in (select distinct Musica.Canta.ID_Utente from Musica.Canta) group by Nick_Name, Sesso, Eta"
    df7 = pd.read_sql(query,conn)

    return jsonify(list(df7.to_dict('index').values()))


#8. Tutti gli album
@app.route('/Album', methods=['GET'])
def Album():
    query=f"select * from Musica.Album"
    df8 = pd.read_sql(query,conn)

    return jsonify(list(df8.to_dict('index').values()))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3246, debug=True)