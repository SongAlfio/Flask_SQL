import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { UtenteComponent } from './utente/utente.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { HomeComponent } from './home/home.component';
import { MusicistaComponent } from './musicista/musicista.component';
import { AlbumComponent } from './album/album.component';
import { SongComponent } from './song/song.component';
import { AddSongComponent } from './add-song/add-song.component';

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
  {
    path: 'Musicista',
    component: MusicistaComponent
  },
  {
    path: 'Home',
    redirectTo: '/Musicista',
    pathMatch: 'full'
  },
  {
    path: 'Album',
    component: AlbumComponent
  },
  {
    path: 'Home',
    redirectTo: '/Album',
    pathMatch: 'full'
  },
  {
    path: 'Song',
    component: SongComponent
  },
  {
    path: 'Home',
    redirectTo: '/Song',
    pathMatch: 'full'
  },
  {
    path: 'Add_Song',
    component: AddSongComponent
  },
  {
    path: 'Home',
    redirectTo: '/Add_Song',
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
