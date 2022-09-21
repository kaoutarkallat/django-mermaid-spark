import { Component, OnInit } from '@angular/core';
import { RegisterService, UserToRegister, SignupModel } from './register.service';
import { Validators, FormBuilder, AbstractControl } from '@angular/forms';

import { Router } from '@angular/router';
import { LoginService } from '../login/login.service';
import { Animations } from '../tools/animations/hover';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  animations:[Animations.errorTrigger]

})
export class RegisterComponent implements OnInit {

  constructor(
    public formBuilder: FormBuilder,
    public signupService: RegisterService,
    public loginService:LoginService,
    public router: Router
  ) { }
  ngOnInit() {
  }

  signupForm = this.formBuilder.group({
    firstName: ['', [Validators.required, Validators.maxLength(30)]],
    lastName: ['', [Validators.required, Validators.maxLength(30)]],
    email: ['', [Validators.required, Validators.email, Validators.maxLength(70)]],
    password: ['', [Validators.required, Validators.minLength(4), Validators.maxLength(30)]],
    cPassword: ['', [Validators.required, Validators.minLength(4), Validators.maxLength(30)]]
  }, {
    validator: PasswordValidation.MatchPassword
  })


  alertOn:boolean=false;
  alertMsg:string='';
  register(user: SignupModel) {
    var userToRegister = new UserToRegister(user.firstName, user.lastName, user.email, user.password)
    this.signupService.registerUser(userToRegister).subscribe(user => {
      console.log(user);
      
      this.router.navigate(['/login']);
    })
  }

  isInvalid(name: string) {
    if (name == "firstName") {
      var firstName = this.signupForm.controls['firstName']
      return firstName.invalid && (firstName.dirty || firstName.touched)
    }
    if (name == "lastName") {
      var lastName = this.signupForm.controls['lastName']
      return lastName.invalid && (lastName.dirty || lastName.touched)
    }
    if (name == "email") {
      var email = this.signupForm.controls['email']
      return email.invalid && (email.dirty || email.touched)
    }
    if (name == "password") {
      var password = this.signupForm.controls['password']
      return password.invalid && (password.dirty || password.touched)
    }
    if (name == "cPassword") {
      var cPassword = this.signupForm.controls['cPassword']
      return cPassword.invalid && (cPassword.dirty || cPassword.touched)
    } else {
      return null
    }
  }

  showError(name: string) {
    if (name == "firstName") {
      var errors = this.signupForm.controls['firstName'].errors
      if (errors) {
        if (errors['required']) return "first name is required"
        else if (errors['maxlength']) return "first name must be at most 30 characters"
        else return null
      }else return null
    }
    else if (name == "lastName") {
      var errors = this.signupForm.controls['lastName'].errors
      if (errors) {
        if (errors['required']) return "last name is required"
        else if (errors['maxlength']) return "last name must be at most 30 characters"
        else return null
      }else return null
    }
    else if (name == "email") {
      var errors = this.signupForm.controls['email'].errors
      if (errors) {

        if (errors['required']) return "email is required"
        else if (errors['email']) return "email is not valid"
        else if (errors['maxlength']) return "email must be at most 70 characters"
        else return null
      }else return null
    }
    else if (name == "password") {
      var errors = this.signupForm.controls['password'].errors
      if (errors) {

        if (errors['required']) return "password is required"
        else if (errors['minlength']) return "password must be at least 4 characters"
        else if (errors['maxlength']) return "password must be at most 30 characters"
        else return null
      }else return null
    }
    else if (name == "cPassword") {
      var errors = this.signupForm.controls['cPassword'].errors
      if (errors) {

        if (errors['required']) return "password is required"
        else if (errors['minlength']) return "password must be at least 4 characters"
        else if (errors['MatchPassword']) return "passwords don't match"
        else if (errors['maxlength']) return ""
        else return null
      }else return null
    } else return null
  }

}

export class PasswordValidation {
  static MatchPassword(AC: AbstractControl) {
    let password = AC.get('password')
    if (password) {
      password = password.value; // to get value in input tag
    } else {
      
    }
    let confirmPassword = AC.get('cPassword'); // to get value in input tag
    if (confirmPassword) {
      confirmPassword = confirmPassword.value
    }
    else {
    
    }
    if (password != confirmPassword) {
      let cpassword = AC.get('cPassword')
      if (cpassword) {

        cpassword.setErrors({ MatchPassword: true })
      }
      else {
        
      }
    } else {
    }
  }
}
