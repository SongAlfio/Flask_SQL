import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css', '../../styles.css']
})
export class HomeComponent  implements OnInit{

  dataForHtml : any;

  constructor(
    private http : HttpClient,
    ){}
  
  ngOnInit(): void {
      this.http.get("https://3245-songalfio-flasksql-j3ybzf1i4ho.ws-eu83.gitpod.io/Search2")
      .subscribe(this.getData)
  }

  getData = (newData : any) =>
  {
      this.dataForHtml = newData;
      console.log(newData);
  }


}
