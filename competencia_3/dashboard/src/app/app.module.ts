import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { ChartLineComponent } from './chart-line/chart-line.component';
import { YearPickerComponent } from './components/year-picker/year-picker.component';

@NgModule({
  declarations: [
    AppComponent,
    ChartLineComponent,
    YearPickerComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
