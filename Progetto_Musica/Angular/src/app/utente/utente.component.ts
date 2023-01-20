import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Component({
  selector: 'app-utente',
  templateUrl: './utente.component.html',
  styleUrls: ['./utente.component.css','../../styles.css','../../../Sign_Up.css']
})
export class UtenteComponent  implements OnInit{
  submitted = false;


  onSubmit(){
  this.submitted = true;
  
  }
  

  
  dataForHtml : any;

  constructor(
    private http : HttpClient,
    ){}
  
  ngOnInit(): void {
      this.http.get("https://3245-songalfio-flasksql-pkk6sj1zv9w.ws-eu83.gitpod.io/Login")

      .subscribe(this.getData)
  }

  getData = (newData : any) =>
  {
      this.dataForHtml = newData;
      console.log(newData);
  }



}


