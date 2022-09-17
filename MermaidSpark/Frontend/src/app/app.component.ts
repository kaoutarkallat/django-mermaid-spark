import { Component, OnInit } from '@angular/core';
import { StopService } from './stop.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'angularshop';

  constructor(public stop: StopService){

  }
  ngOnInit() {
    this.stop.get_all_products()
  }
}
