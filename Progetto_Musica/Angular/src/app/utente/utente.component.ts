import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';



@Component({
  selector: 'app-utente',
  templateUrl: './utente.component.html',
  styleUrls: ['./utente.component.css','../../styles.css','../../../Sign_Up.css']
})
export class UtenteComponent  implements OnInit{
  query = ''; 
  dataForHtml : any;

  constructor(private http : HttpClient){}
  
  ngOnInit(): void {
    if (this.query !== '') {
      this.http.get("https://3245-songalfio-flasksql-es64wx21h3x.ws-eu82.gitpod.io/Login/" + this.query)
  }
  }

  getData = (newData : any) =>
  {
      this.dataForHtml = newData;
      console.log(newData);
  }


}
export class SimpleFormComp {
  onSubmit(f: NgForm) {
    console.log(f.value);  // { first: '', last: '' }
    console.log(f.valid);  // false
  }
}
