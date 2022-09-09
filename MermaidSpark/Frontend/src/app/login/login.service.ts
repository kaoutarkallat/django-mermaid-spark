import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators'
// import { tokenNotExpired } from 'angular2-jwt';

import { JwtHelperService } from '@auth0/angular-jwt';
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  theToken:any;
  theUser:any;
  
  // *******  is TWA *******
  isTWA:boolean |undefined;
  
  constructor(public http:HttpClient) { }
  authenticateUser(user: UserLg):Observable<TokenRes>{
    return this.http.post<TokenRes>("/user/authentication", user).pipe(
      catchError((e)=>this.errorHandler(e)))
  }

  helper = new JwtHelperService();
  // loggedIn(token){
  //   return tokenNotExpired(token);
  // }
  loggedIn(tokenName: string){
    var token = localStorage.getItem(tokenName); 
    return token != null && !this.helper.isTokenExpired(token)&&false;
    // return tokenNotExpired(token);
  }

  getUserProfile():Observable<UserPr>{
    this.theToken=localStorage.getItem('id_token');
    let headers=new HttpHeaders();
    let headers_auth=headers.append("Authorization",this.theToken);
    console.log(headers_auth.get('Authorization'));
    return this.http.get<UserPr>("/users/profile", {headers:headers_auth})
    .pipe(
      catchError((e)=>this.errorHandler(e))
      )
  }

  // ************  monitor clicks ****************
  // ************  monitor clicks ****************
  // ************  monitor clicks ****************

  addClick(name:string,type:string,clickId?:string){
    const httpOptions={
      headers:new HttpHeaders({"content-type":"application/json"})
    }
    return this.http.post<any>('/user/addClick',{name:name,type:type,clickId:clickId},httpOptions).pipe(
      catchError((e)=>this.errorHandler(e)))
  }

  updateClick(clickId?:string){
    const httpOptions={
      headers:new HttpHeaders({"content-type":"application/json"})
    }
    return this.http.post<any>('/user/updateClick',{clickId:clickId},httpOptions).pipe(
      catchError((e)=>this.errorHandler(e)))
  }

  monitorClick(name:string,type:string,clickId?:string){
    this.addClick(name,type,clickId).subscribe(()=>{})
  }


  storeUserData(token:string, user:UserRes,profileId:string,MyminProfile:MinProfile){
    localStorage.setItem('id_token', token)
    localStorage.setItem('user', JSON.stringify(user))
    localStorage.setItem('profileId', profileId)
    localStorage.setItem('MyminProfile', JSON.stringify(MyminProfile))
    this.theToken=token;
    this.theUser=user;
  }
  
  logoutUser(){
    this.theToken=null;
    this.theUser=null;
    localStorage.clear();
  }
  addToWaitingList(fullName:string,email:string){
    const httpOptions={
      headers:new HttpHeaders({"content-type":"application/json"})
    }
    return this.http.post<any>('/user/emails',{fullName:fullName,email:email},httpOptions).pipe(
      catchError((e)=>this.errorHandler(e)))
  }

  requestPassword(email:string){
    const httpOptions={
      headers:new HttpHeaders({"content-type":"application/json"})
    }
    return this.http.post<any>('/user/lostpassword',{email:email},httpOptions).pipe(
      catchError((e)=>this.errorHandler(e)))
  }

  errorHandler(error: HttpErrorResponse){
    return throwError(error.message);
  }
  
}

export interface UserLg{
  email: string | null,
  password: string | null
}
export interface TokenRes{
  success:Boolean,
  msg:string,
  token:string,
  user:UserRes,
  profileId:string,
  MyminProfile:MinProfile
}
export interface UserRes{
  name:string,
  firstName:string,
  lastName:string,
  email:string,
  role:string
}

export interface UserPr{
  name:string,
  email:string,
  firstName:string,
  lastName:string,
  password:string,
  _id:string,
  _v:string
}

export interface MinProfile{
  _id?:string,
  firstName?:string,
  lastName?:string,
  country?:string,
  online?:boolean,
  offlineDate?:Date,
  profilePhoto?:any,
  role?:string,
}