import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';


interface GoldPrice {
  year: number;
  real_value_usd: number;
  nominal_value_usd: number
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  file: string = "assets/json/gold_prices.json"
  stocks: GoldPrice[] = []

  years!: number[];
  prices!: number[];

  firstYear!: number;
  lastYear!: number;

  minYear!: number;
  maxYear!: number;
  valueType: string = "nominal";

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<Array<GoldPrice>>(this.file)
      .subscribe((stocksFound) => {
        this.stocks = stocksFound;
        this.firstYear = this.stocks[0].year;
        this.lastYear = this.stocks[this.stocks.length-1].year;
        this.minYear = this.firstYear;
        this.maxYear = this.lastYear;

        this.applyFilter();
      })
  }

  onChangeMinYear(year: number) {
    this.minYear = year;
    this.applyFilter();

  }

  onChangeMaxYear(year: number) {
    this.maxYear = year;
    this.applyFilter();

  }

  onChangeValueType(event: any) {
    this.valueType = event.target.value;
    this.applyFilter();

  }

  applyFilter() {
    this.years = [];
    this.prices = [];
    this.stocks.forEach(stock => {
      if (this.isInRange(stock.year, this.minYear, this.maxYear)) {
        this.years.push(stock.year);

        switch (this.valueType) {
          case 'nominal':
            this.prices.push(stock.nominal_value_usd);
            break;
          case 'real':
            this.prices.push(stock.real_value_usd);
            break;
        }
      }
    })

  }

  private isInRange(year: number, min: number, max: number) {
    return year >= min && year <= max;

  }

}
