import { Component, OnInit } from '@angular/core';
import { StopService } from '../stop.service';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent implements OnInit {

  constructor(public stop:StopService) { }

  ngOnInit(): void {
  }

}
