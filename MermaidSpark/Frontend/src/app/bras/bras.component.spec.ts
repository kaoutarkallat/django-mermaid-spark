import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BrasComponent } from './bras.component';

describe('BrasComponent', () => {
  let component: BrasComponent;
  let fixture: ComponentFixture<BrasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BrasComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BrasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
