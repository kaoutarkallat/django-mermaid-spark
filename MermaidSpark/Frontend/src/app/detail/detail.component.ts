import { Component, OnInit } from '@angular/core';
import { DataService } from '../home/data.service';
import { StopService } from '../stop.service';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {

  constructor(public stop: StopService) { }
  images:string[]=[]
  quantity=1
  ngOnInit(): void {
    this.stop.is_home=false
    window.scroll({'top':0})
    console.log(this.stop.product_detail)
    this.images=[this.stop.product_detail.img_front,this.stop.product_detail.img_back]
    console.log(this.images)
  }
  increase_quantity(){
    this.quantity+=1
  }
  decrease_quantity(){
    if(this.quantity>1){
      this.quantity-=1
    }
  }

  add_to_cart(){
    console.log("cart:")
    this.stop.cart.push(this.stop.product_detail)
    console.log(this.stop.cart)
    
  }

  star_list = ['',
  'a-icon-star-medium a-star-medium-1',
  'a-icon-star-medium a-star-medium-2',
  'a-icon-star-medium a-star-medium-3',
  'a-icon-star-small a-star-small-4',
  'a-icon-star-small a-star-small-5'
]

}
