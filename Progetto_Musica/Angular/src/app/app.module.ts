import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'; 
import { AppComponent } from './app.component';
import { RouterModule } from '@angular/router';
import { UtenteComponent } from './utente/utente.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { AppRoutingModule } from './app-routing.module';
import { HomeComponent } from './home/home.component';
import { CarouselComponent } from './carousel/carousel.component';
import { MusicistaComponent } from './musicista/musicista.component';
import { NotificheComponent } from './notifiche/notifiche.component';
import { AlbumComponent } from './album/album.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SongComponent } from './song/song.component';
import { AddSongComponent } from './add-song/add-song.component';

import { NavBarComponent } from './nav-bar/nav-bar.component';

@NgModule({
  declarations: [
    AppComponent,
    UtenteComponent,
    SignUpComponent,
    HomeComponent,
    CarouselComponent,
    MusicistaComponent,
    NotificheComponent,
    AlbumComponent,
    SongComponent,
    AddSongComponent,
    NavBarComponent,

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
      BrowserModule,
      FormsModule,
      ReactiveFormsModule,
      RouterModule.forRoot([
        {path: 'Utente', component: UtenteComponent},
        {path: 'Sign_Up', component: SignUpComponent},
        {path: 'Musicista', component: MusicistaComponent},
        {path: 'Notifiche', component: NotificheComponent},
        {path: 'Album', component: AlbumComponent},
        {path: 'Song', component: SongComponent},
        {path: 'Add_Song', component: AddSongComponent},

        {path: 'Utente', redirectTo: '/Utente', pathMatch: 'full'},
        {path: 'Sign_Up', redirectTo: '/Sign_Up', pathMatch: 'full'},
        {path: 'Musicista', redirectTo: '/Musicista', pathMatch: 'full'},
        {path: 'Notifiche', redirectTo: '/Notifiche', pathMatch: 'full'},
        {path: 'Album', redirectTo: '/Album', pathMatch: 'full'},
        {path: 'Song', redirectTo: '/Song', pathMatch: 'full'},
        {path: 'Add_Song', redirectTo: '/Add_Song', pathMatch: 'full'},

      ]),
      AppRoutingModule
    ],
  
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { 
  
}
export * from './app.component';
export * from './sign-up/sign-up.component';
export * from './utente/utente.component';
export * from './musicista/musicista.component';



