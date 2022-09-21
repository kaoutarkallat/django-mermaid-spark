import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { catchError } from 'rxjs/operators'

@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  constructor(public http:HttpClient) { }

  registerUser(user:UserToRegister):Observable<UserToRegister>{
    const httpOptions={
      headers:new HttpHeaders({"content-type":"application/json"})
    }
    return this.http.post<UserToRegister>('/api/user/register',user,httpOptions).pipe(
      catchError((e)=>this.errorHandler(e)))
  }

  errorHandler(error: HttpErrorResponse){
    return throwError(error.message);
  }
}

export class SignupModel{
  constructor(
    public firstName:string,
    public lastName:string,
    public email:string,
    public password:string,
    public cPassword:string
    ){}
}
export class UserToRegister{
  constructor(
    public firstName:string,
    public lastName:string,
    public email:string,
    public password:string
    ){}
}

