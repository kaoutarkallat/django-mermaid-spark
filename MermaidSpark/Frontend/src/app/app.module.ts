import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { HomeComponent } from './home/home.component';
import { SlickCarouselModule } from 'ngx-slick-carousel';
import { DataService } from './home/data.service';
import { DetailComponent } from './detail/detail.component';
import { ContactComponent } from './contact/contact.component';
import { StopService } from './stop.service';
import { RefundPolicyComponent } from './refund-policy/refund-policy.component';
import { PrivacyPolicyComponent } from './privacy-policy/privacy-policy.component';
import { CartComponent } from './cart/cart.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { LeggingsComponent } from './leggings/leggings.component';
import { ShortsComponent } from './shorts/shorts.component';
import { BrasComponent } from './bras/bras.component';
import { TankTopsComponent } from './tank-tops/tank-tops.component';
import { SneakersComponent } from './sneakers/sneakers.component';
import { AccessoriesComponent } from './accessories/accessories.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpBackend, HttpClientModule } from '@angular/common/http';
import { MoreProductsComponent } from './more-products/more-products.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    DetailComponent,
    ContactComponent,
    RefundPolicyComponent,
    PrivacyPolicyComponent,
    CartComponent,
    CheckoutComponent,
    LeggingsComponent,
    ShortsComponent,
    BrasComponent,
    TankTopsComponent,
    SneakersComponent,
    AccessoriesComponent,
    AboutUsComponent,
    LoginComponent,
    RegisterComponent,
    MoreProductsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SlickCarouselModule,
    BrowserAnimationsModule,
    FormsModule, ReactiveFormsModule,
    HttpClientModule

  ],
  providers: [DataService, StopService],
  bootstrap: [AppComponent]
})
export class AppModule { }
