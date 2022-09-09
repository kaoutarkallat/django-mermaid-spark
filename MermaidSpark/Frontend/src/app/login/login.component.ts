
import { Component, OnInit } from '@angular/core';
import { Validators, FormBuilder } from '@angular/forms';
import { UserLg, TokenRes, LoginService } from './login.service';
import { Router } from '@angular/router';

import { Meta, Title } from '@angular/platform-browser';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(
    public formBuilder:FormBuilder,
    public loginService:LoginService,
    public router: Router,
   
    public title: Title, 
    public meta: Meta
  ) { }
  singupInfoOn:boolean=false;
  forgotPassworkOn:boolean=false
  ngOnInit() {
    console.log('blabla')
    this.title.setTitle('MetricGate: Login')
    this.meta.updateTag({
      name:"description",
      content:"Log in to your MetricGate account and start analysing your dataset."
    })
  }
  go2signup=() =>{
    this.singupInfoOn=true;
  }
  closeForgotPassword=() =>{
    this.forgotPassworkOn=false;
  }
  openForgotPassword=() =>{
    this.loginService.monitorClick('forgotpassword','btn')
    this.forgotPassworkOn=true;
  }  
  
  loginForm=this.formBuilder.group({
    email:['',[Validators.required]],
    password:['',[Validators.required]],
  })

  alertOn:boolean=false;
  alertMsg:string | undefined;
  login(user:UserLg | any){
    console.log(user)
    this.loginService.authenticateUser(user).subscribe(data=>{
      var tokenRes:TokenRes=data;
      if(tokenRes.success){
        console.log(tokenRes);
        this.loginService.storeUserData(tokenRes.token,tokenRes.user,tokenRes.profileId,tokenRes.MyminProfile);
        // this.flashMessage.success("You're now logged in",{delay:3000,navigate:'/profile'});
        // this.savedtoken=tokenRes.token;
        this.router.navigate(['/platform/data/data-editor']);
      
       
      }
      else{
        console.log(tokenRes);
        this.alertMsg=tokenRes.msg
        this.alertOn=true;
        setTimeout(() => {
          this.alertOn=false
        }, 3000);
        // this.flashMessage.danger(tokenRes.msg,{delay:3000});
      }
    })
  }

  // ************************  request to register an account  *********************
  // ************************  request to register an account  *********************
  // ************************  request to register an account  *********************
  
  fullName:string=""
  notRegisteredEmail:string=""
  addToWaitingList(){
    if(this.notRegisteredEmail.length<80&&this.notRegisteredEmail.length>5){
      this.loginService.addToWaitingList(this.fullName,this.notRegisteredEmail).subscribe((data)=>{
        console.log(this.fullName,this.notRegisteredEmail)
      })
      this.fullName=""
      this.notRegisteredEmail=""
    }
  }
  
  // ************************  request to change password  *********************
  // ************************  request to change password  *********************
  // ************************  request to change password  *********************
  requestPasswordEmail:string=""
  requestPassword(){
    if(this.requestPasswordEmail.length<80&&this.requestPasswordEmail.length>10){
      this.loginService.requestPassword(this.requestPasswordEmail).subscribe((data)=>{
        console.log(this.requestPasswordEmail)
      })
      this.requestPasswordEmail=""
    }
  }


}
