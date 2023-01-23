import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-album',
  templateUrl: './album.component.html',
  styleUrls: ['./album.component.css']
})
export class AlbumComponent implements OnInit{

  dataForHtml : any;

  constructor(
    private http : HttpClient,
    ){}
  
  ngOnInit(): void {
      this.http.get("https://3246-songalfio-flasksql-x2vaxjn8uet.ws-eu83.gitpod.io/Album")

      .subscribe(this.getData)
  }

  getData = (newData : any) =>
  {
      this.dataForHtml = newData;
      console.log(newData);
  }

}
