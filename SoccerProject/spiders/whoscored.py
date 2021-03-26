import scrapy
import json
import gzip
from scrapy import Request, Spider
from SoccerProject.items import *

class WhoscoredSpider(scrapy.Spider):
    name = 'whoscored'
    allowed_domains = ['whoscored.com']

    squad_offensive_url = 'https://www.whoscored.com/StatisticsFeed/1/GetPlayerStatistics?' \
                          'category=summary&subcategory=defensive&statsAccumulationType=0&i' \
                          'sCurrent=true&playerId=&teamIds=30&matchId=&stageId=&tournamentOpti' \
                          'ons=2&sortBy=tacklePerGame&sortAscending=false&age=&ageComparisonType=' \
                          '&appearances=&appearancesComparisonType=&field=Overall&nationality=&positi' \
                          'onOptions=&timeOfTheGameEnd=&timeOfTheGameStart=&isMinApp=false&page=&include' \
                          'ZeroValues=true&numberOfPlayersToPick='

    def start_requests(self):
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.87 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        yield Request(self.squad_offensive_url, callback=self.parse_squad, headers=headers)

    def parse_squad(self, response):
        self.logger.debug(response)
        print('1')
        print(response.text)
        print('2')
        print(response.text)
        try:
            result = json.loads(response.text)
        except:
            pass

        player_item = SquadItem()
        # for player in result['playerTableStats']:
        #     player_item['ID'] = player['playerID']
        #     player_item['name'] = player['name']

        yield player_item
