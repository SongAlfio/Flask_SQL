import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { UtenteComponent } from './utente/utente.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {
    path: 'Home',
    component: HomeComponent
  },
  {
    path: '',
    redirectTo: '/Home',
    pathMatch: 'full'
  },
  {
    path: 'Utente',
    component: UtenteComponent
  },
  {
    path: 'Home',
    redirectTo: '/Utente',
    pathMatch: 'full'
  },
  {
    path: 'Sign_Up',
    component: SignUpComponent
  },
  {
    path: 'Home',
    redirectTo: '/Sign_Up',
    pathMatch: 'full'
  },
];

  @NgModule({
      declarations: [],
      imports: [
        CommonModule,
        RouterModule.forRoot(routes)
      ],
      exports: [RouterModule]
    })
export class AppRoutingModule { }
