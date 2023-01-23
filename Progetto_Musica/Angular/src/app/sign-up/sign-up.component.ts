import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css','../../../Sign_Up.css','../../styles.css']
})
export class SignUpComponent {
  profileForm = new FormGroup({
    Nome_utente: new FormControl(''),
    Email: new FormControl(''),
    Password: new FormControl(''),
    Età: new FormControl(''),
    Sesso: new FormControl(''),

  });
  //Update Nome
//updateName() {
//  this.name.setValue('Nancy');
//}
onSubmit() {
  // TODO: Use EventEmitter with form value
  console.warn(this.profileForm.value);
}
}
