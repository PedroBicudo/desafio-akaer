import { Component, ElementRef, Input, OnChanges, OnInit, SimpleChanges, ViewChild } from '@angular/core';
import Chart, { LogarithmicScale } from 'chart.js/auto';

@Component({
  selector: 'app-chart-line',
  templateUrl: './chart-line.component.html',
  styleUrls: ['./chart-line.component.css']
})
export class ChartLineComponent implements OnInit, OnChanges {

  @Input()
  prices!: number[];

  @Input()
  years!: number[];

  chart!: Chart;

  @ViewChild("myChart", {static: true})
  chartCanvas!: ElementRef;

  constructor() { }

  ngOnInit(): void {
    const data = {
      labels: this.years,
      datasets: [{
        label: `Historical gold price from 1791 to 2020 in USD`,
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: this.prices
      }]
    }


    this.chart = new Chart(
      this.chartCanvas.nativeElement,
      {
        type: 'line',
        data: data,
      }
    )
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (!this.chart) return;
    this.chart.data.datasets[0].data = this.prices;
    this.chart.data.datasets[0].label = `Historical gold price from ${this.years[0]} to ${this.years[this.years.length-1]} in USD`;
    this.chart.data.labels = this.years;
    this.chart.update();

  }


}
