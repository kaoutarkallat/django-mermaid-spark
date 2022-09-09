import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TankTopsComponent } from './tank-tops.component';

describe('TankTopsComponent', () => {
  let component: TankTopsComponent;
  let fixture: ComponentFixture<TankTopsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TankTopsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TankTopsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
