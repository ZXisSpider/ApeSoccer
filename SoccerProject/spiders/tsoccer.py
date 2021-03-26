import scrapy
import json
import gzip
from scrapy import Request, Spider
from SoccerProject.items import *
from SoccerProject.config import *

class TsoccerSpider(scrapy.Spider):
    name = 'tsoccer'
    allowed_domains = ['tzuqiu.cc']

    teamstats_url = 'http://www.tzuqiu.cc/teams/{tid}/teamStats.do'
    team_matchstats_url = 'http://www.tzuqiu.cc/{teams}/{tid}/fixture.do'
    config = Soccerconfig()
    team_dict = config.team2id_dict
    premier_teamID = config.premier_teamID
    All_teamID = config.All_teamID

    def start_requests(self):
        headers = self.config.headers

        for tid in self.All_teamID:
            yield Request(self.teamstats_url.format(tid=tid), callback=self.parse_team, headers=headers)
            # yield Request(self.team_matchstats_url.format(tid=tid), callback=self.parse_team_match, headers=headers)

    def parse_team(self, response):
        self.logger.debug(response)
        selector = response.selector
        team_stats = selector.re_first('teamStat = .*;')
        team_stats = '{' + team_stats.split('{')[1].split('}')[0] + '}'
        team_stats = eval(team_stats)

        print(team_stats)

        team_item = TeamItem()

        field_map = self.config.team_field_map
        for field, attr in field_map.items():
            team_item[field] = team_stats.get(attr)
        team_item['name'] = self.config.id2team_dict.get(team_stats.get('teamId'))
        team_item['league_name'] = self.config.judgeleague(team_stats.get('teamId'))

        yield team_item

    def parse_team_match(self, response):
        self.logger.debug(response)


    def parse_player(self, response):
        pass



