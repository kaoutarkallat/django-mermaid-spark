import { Component, OnInit } from '@angular/core';
import { DataService } from '../home/data.service';
import { StopService } from '../stop.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor(public stop: StopService) {}
  toggle= true
  open_menu = true
  ngOnInit(): void {
  }

}
