import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutUsComponent } from './about-us/about-us.component';
import { AccessoriesComponent } from './accessories/accessories.component';
import { BrasComponent } from './bras/bras.component';
import { CartComponent } from './cart/cart.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { ContactComponent } from './contact/contact.component';
import { DetailComponent } from './detail/detail.component';
import { HomeComponent } from './home/home.component';
import { LeggingsComponent } from './leggings/leggings.component';
import { LoginComponent } from './login/login.component';
import { MoreProductsComponent } from './more-products/more-products.component';
import { PrivacyPolicyComponent } from './privacy-policy/privacy-policy.component';
import { RefundPolicyComponent } from './refund-policy/refund-policy.component';
import { RegisterComponent } from './register/register.component';
import { ShortsComponent } from './shorts/shorts.component';
import { SneakersComponent } from './sneakers/sneakers.component';
import { TankTopsComponent } from './tank-tops/tank-tops.component';

const routes: Routes = [
  {  path:"", component:HomeComponent} ,
  { path:"cart", component:CartComponent},
  { path:"home", component:HomeComponent},
  { path:"checkout", component:CheckoutComponent},
  { path:"products/:id", component:HomeComponent},
  { path:"more-products/:id", component:MoreProductsComponent},
  { path:"leggings/:id", component:LeggingsComponent},
  { path:"bras/:id", component:BrasComponent},
  { path:"shorts/:id", component:ShortsComponent},
  { path:"tank_tops/:id", component:TankTopsComponent},
  { path:"sneakers/:id", component:SneakersComponent},
  { path:"accessories/:id", component:AccessoriesComponent},
  { path:"refund-policy", component:RefundPolicyComponent},
  { path:"privacy-policy", component:PrivacyPolicyComponent},
  { path:"detail", component:DetailComponent},
  { path:"detail/:id", component:DetailComponent},
  { path:"contact", component:ContactComponent},
  { path:"about-us", component:AboutUsComponent},
  {path:"login", component:LoginComponent},
  {path:"register", component:RegisterComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes,{
    useHash:false,
    onSameUrlNavigation: 'reload',
  anchorScrolling:'enabled'  
  })],
  exports: [RouterModule]
})
export class AppRoutingModule {


 }
