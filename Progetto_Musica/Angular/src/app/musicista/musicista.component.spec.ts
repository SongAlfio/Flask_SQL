import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MusicistaComponent } from './musicista.component';

describe('MusicistaComponent', () => {
  let component: MusicistaComponent;
  let fixture: ComponentFixture<MusicistaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MusicistaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MusicistaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
