import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';



@Component({
  selector: 'app-utente',
  templateUrl: './utente.component.html',
  styleUrls: ['./utente.component.css','../../styles.css','../../../Sign_Up.css']
})
export class UtenteComponent  implements OnInit{
  dataForHtml : any;

  constructor(private http : HttpClient){}
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }
  



}


