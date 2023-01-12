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

@NgModule({
  declarations: [
    AppComponent,
    UtenteComponent,
    SignUpComponent,
    HomeComponent,
    CarouselComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
      BrowserModule,
      RouterModule.forRoot([
        {path: 'Utente', component: UtenteComponent},
        {path: 'Sign_Up', component: SignUpComponent},
        {path: 'Utente', redirectTo: '/Utente', pathMatch: 'full'},
        {path: 'Sign_Up', redirectTo: '/Sign_Up', pathMatch: 'full'},
      ]),
      AppRoutingModule,
    ],
  
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { 
  
}
export * from './app.component';
export * from './sign-up/sign-up.component';
export * from './utente/utente.component';