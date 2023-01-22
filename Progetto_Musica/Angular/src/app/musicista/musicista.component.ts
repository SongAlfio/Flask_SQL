import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-musicista',
  templateUrl: './musicista.component.html',
  styleUrls: ['./musicista.component.css']
})
export class MusicistaComponent  implements OnInit{

  dataForHtml : any;

  constructor(private http : HttpClient){}
  
  ngOnInit(): void {
      this.http.get("https://3246-songalfio-flasksql-w9acazq4wi3.ws-eu83.gitpod.io/Musicisti")
      .subscribe(this.getData)
  }

  getData = (newData : any) =>
  {
      this.dataForHtml = newData;
      console.log(newData);
  }


}
