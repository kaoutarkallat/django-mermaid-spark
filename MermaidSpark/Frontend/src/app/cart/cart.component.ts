import { Component, OnInit } from '@angular/core';
import { StopService } from '../stop.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {

  constructor(public stop:StopService) { }

  ngOnInit(): void {
  }

}
