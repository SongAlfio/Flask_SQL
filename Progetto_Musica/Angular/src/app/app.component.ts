import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  staffs!: any;
  loading!: Boolean;
  url: string = "https://3245-songalfio-flasksql-j9ucuwz5uz7.ws-eu78.gitpod.io/";

  constructor(public http: HttpClient) {
    this.get(this.url);
  }

  get(url: string): void {
    this.loading = true;
    this.http.get(url).subscribe(data => {
      this.staffs = data;
      this.loading = false;
    });
  }

  // previousSearch: string = '';
  // onKey(value: string) {
  //   if (value != this.previousSearch) {
  //     this.get(this.url + "?store_name=" + value);
  //     this.previousSearch = value;
  //   }
  // }

  onKey(value: string) {
    this.get(this.url + "?store_name=" + value);
  }
}