import { Component } from '@angular/core';
import { NewsService } from './newsfeed.service';

@Component({
  selector: 'app-newsfeed',
  templateUrl: 'newsfeed.page.html',
  styleUrls: ['newsfeed.page.scss']
})
export class NewsfeedPage {
  newsfeed: any[];
  
  constructor(private newsService: NewsService) {
    this.newsfeed = newsService.news;
    this.newsService.getNews();
    this.newsService.getTwitter();
    this.newsService.getNewsUpdate().subscribe(
      data => {
        this.newsfeed = data;
      }
    );
  }
}
