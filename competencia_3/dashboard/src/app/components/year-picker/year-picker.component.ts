import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-year-picker',
  templateUrl: './year-picker.component.html',
  styleUrls: ['./year-picker.component.css']
})
export class YearPickerComponent implements OnInit {

  @Input()
  yearStart!: number;

  @Input()
  yearEnd!: number;

  @Input()
  yearCurr!: number;

  @Input()
  label!: string;

  @Output()
  yearEmitter = new EventEmitter<number>();

  constructor() { }

  ngOnInit(): void {
    this.yearCurr = this.yearEnd;
  }

  onChangeYear(value: number) {
    let result = this.yearCurr + value;
    if (result < this.yearStart || result > this.yearEnd) return;
    this.yearCurr = result;
    this.yearEmitter.emit(this.yearCurr);
  }

}
