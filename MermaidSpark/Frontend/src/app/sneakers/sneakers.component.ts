import { Component, OnInit } from '@angular/core';
import { StopService } from '../stop.service';

@Component({
  selector: 'app-sneakers',
  templateUrl: './sneakers.component.html',
  styleUrls: ['./sneakers.component.css']
})
export class SneakersComponent implements OnInit {

  constructor(public stop: StopService) { }


  category = 'sneakers'
  ngOnInit(): void {
    // window.scroll({'top':0}s)
    this.stop.category = ["sneakers"]

    this.stop.get_page(this.stop.page_num)
    // this.products_page = this.products.filter((value,index)=>(index<9) && value.type=='leggings')
  }

  next() {
    this.stop.page_num += 1
    this.stop.get_page(this.stop.page_num)
  }
  previous() {
    this.stop.page_num -= 1
    this.stop.get_page(this.stop.page_num)
  }

  star_size = 'a-icon-star-medium a-star-medium-1'
  star_dict = {
    '1': 'a-icon-star-medium a-star-medium-1',
    '2': 'a-icon-star-medium a-star-medium-2',
    '3': 'a-icon-star-medium a-star-medium-3',
    '4': 'a-icon-star-small a-star-small-4',
    '4.5': 'a-icon-star-small a-star-small-4-5',
    '5': 'a-icon-star-small a-star-small-5'
  }
  star_list = ['',
    'a-icon-star-medium a-star-medium-1',
    'a-icon-star-medium a-star-medium-2',
    'a-icon-star-medium a-star-medium-3',
    'a-icon-star-small a-star-small-4',
    'a-icon-star-small a-star-small-5'
  ]
 

}
