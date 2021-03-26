import json
import requests
from requests.exceptions import RequestException
import re
import time
from lxml import etree
from SoccerProject.config import *
from pyquery import PyQuery as pq

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
        html = etree.HTML(html)
        # result = html.xpath('//a[@class="sm_logo-name sm_logo-name-flag sm-hide-logo-datatable"]/@href')
        team_names = html.xpath('//a[contains(@href, "teams") and\
         @class="sm_logo-name sm_logo-name-flag sm-hide-logo-datatable"]/@title')
        team_nums = html.xpath('//a[contains(@href, "teams") and\
         @class="sm_logo-name sm_logo-name-flag sm-hide-logo-datatable"]/@href')
        for i in range(len(team_nums)):
            team_nums[i] = team_nums[i].strip('/teams/').strip('/show.do')
        z = dict(zip(team_names, team_nums))

        team_nums = list(set(team_nums))
        print('联赛有' + str(len(team_nums)) + '只球队')
        for i in range(len(team_nums)):
            team_nums[i] = int(team_nums[i])
        print(team_nums)
        for key,value in z.items():
            print('\'' + str(key) + '\': ' + str(int(value)) + ',')

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://www.tzuqiu.cc/competitions/'+ str(offset) +'/show.do'
    html = get_one_page(url)
    parse_one_page(html)
    # for item in parse_one_page(html):
    #     print(item)
        # write_to_file(item)


if __name__ == '__main__':
    config = Soccerconfig()
    matchdict = config.match2id_dict
    matches = list(config.match2id_dict.values())
    print(matchdict)
    for i in matches:
        main(offset=i)
        time.sleep(1)