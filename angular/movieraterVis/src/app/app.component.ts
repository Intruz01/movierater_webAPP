import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  movies = [{title: 'its not working'}];

  constructor(private api: ApiService){
    this.getMovies();
  }
  getMovies = () => {
    this.api.getAllMovies().subscribe (
      data => {
        this.movies = data;
      },
      error => {
        console.log(error);
      }
    );
  }

  movieClicked = (movie) => {
    this.api.getOneMovie(movie.id).subscribe (
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}
