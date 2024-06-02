import requests
from bs4 import BeautifulSoup
import re
import csv

class SteamstoreScraper:
    def __init__(self):
        self.base_url = "https://store.steampowered.com/search/?category1=998&supportedlang=english&ndl=1&page={}"
        self.page_number = 1
        self.session = requests.Session()

    def fetch_page(self, url):
        response = self.session.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def parse_game(self, game):
        game_data = {
            'name': game.select_one('span.title').get_text(strip=True),
            'link': game['href'],
            'price': (game.select_one('div.discount_original_price') or game.select_one('div.discount_final_price')).get_text(strip=True) if (game.select_one('div.discount_original_price') or game.select_one('div.discount_final_price')) else '',
            'review_count_raw': '',
            'review_count': '',
            'review_percentage': '',  
            'game_tags': []
        }
        game_link = game['href']
        game_details = self.fetch_page(game_link)
        if game_details:
            game_soup = BeautifulSoup(game_details, 'html.parser')
            review_count_meta = game_soup.select_one('div[itemprop="aggregateRating"] meta[itemprop="reviewCount"]')
            if review_count_meta:
                review_count_raw = review_count_meta['content']
                review_count = re.search(r'\d+', review_count_raw).group() if review_count_raw else ""
                game_data['review_count'] = review_count
                
                summary_column = game_soup.select_one('.summary.column')
                if summary_column:
                    review_percentage_text = summary_column.find(string=re.compile(r'\d+%'))
                    if review_percentage_text:
                        review_percentage = re.search(r'\d+%', review_percentage_text).group()
                        game_data['review_percentage'] = review_percentage

            game_tags_raw = [tag.get_text(strip=True) for tag in game_soup.select('a.app_tag')]
            game_data['game_tags'] = game_tags_raw
        return game_data

    def scrape(self, max_pages=1):
        while self.page_number <= max_pages:
            url = self.base_url.format(self.page_number)
            page_content = self.fetch_page(url)
            if not page_content:
                break

            soup = BeautifulSoup(page_content, 'html.parser')
            games = soup.select('a.search_result_row')
            if not games:
                break

            for game in games:
                game_data = self.parse_game(game)
                yield game_data

            self.page_number += 1

if __name__ == "__main__":
    scraper = SteamstoreScraper()
    max_pages = 1000
    
    with open('0_1000pageoutput.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        first_iteration = True
        
        for data in scraper.scrape(max_pages):
            if first_iteration:
                writer.writerow(data.keys())
                first_iteration = False
            
            writer.writerow(data.values())
            
            print(data)
