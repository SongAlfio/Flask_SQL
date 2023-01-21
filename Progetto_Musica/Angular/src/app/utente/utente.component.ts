import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Data } from 'src/models/request.model';
import { ManagerService } from 'src/services/manager.service';

@Component({
  selector: 'app-utente',
  templateUrl: './utente.component.html',
  styleUrls: ['./utente.component.css','../../styles.css','../../../Sign_Up.css']
})
export class UtenteComponent implements OnInit {
  form!: FormGroup;
  errorMessage!: string;
  statusCode!: number;

  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private manager: ManagerService
  ) { }

  ngOnInit(): void {
    // Controllo se l'utente ha gia' eseguito il login
    if (this.manager.getUser.id != -1) this.router.navigate(['/dashboard']);

    // Inizializzo la form
    this.form = this.fb.group({
      email: ["", [Validators.required, Validators.email]],
      password: ["", [Validators.required]],
    })
  }

  submit() {
    // Creo l'oggetto che verra' inviaro al server Flask con le credenziali delll'utente
    let body: HttpParams = new HttpParams().appendAll({
      'email': this.form.value.email,
      'password': this.form.value.password
    });

    // Eseguo la richiesta in POST
    this.http.post<Data>('http://127.0.0.1:3245/Login_Page', '', {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      params: body,
      responseType: "json"
    }).subscribe(data => {
      // Aspetto la risposta del server e comunico all'utente la risposta
      if (data.statusCode == 200) {
        // Invio le informazioni dell'utente alle pagine in ascolto
        this.manager.setUser(data.data);

        // Reindirizzo l'utente alla sua dashboard
        this.router.navigate(['/dashboard']);
      } else {
        this.statusCode = data.statusCode;
        this.errorMessage = data.errorMessage;
      }
    });
  }

}


