# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class TeamItem(scrapy.Item):
    collection = 'team_stats'

    name = Field()
    league_name = Field()
    aerialWon = Field()
    aerialWonPtn = Field()
    apps = Field()
    assists = Field()
    assistsPtn = Field()
    ballRecovery = Field()
    ballRecoveryPtn = Field()
    bigChanceCreated = Field()
    bigChanceCreatedPtn = Field()
    bigChanceMissed = Field()
    bigChanceMissedPtn = Field()
    bigChanceScored = Field()
    bigChanceScoredPtn = Field()
    bigChanceSucc = Field()
    bigChanceSuccPtn = Field()
    cardPtn = Field()
    clears = Field()
    clearsPtn = Field()
    competitionId = Field()
    competitionIdWs = Field()
    createTime = Field()
    defensiveThirdPass = Field()
    defensiveThirdPassAcc = Field()
    defensiveThirdPassSucc = Field()
    defensiveThirdPassSuccPtn = Field()
    dribbles = Field()
    dribblesPtn = Field()
    errorsSum = Field()
    errorsSumPtn = Field()
    fatalError = Field()
    finalThirdPass = Field()
    finalThirdPassAcc = Field()
    finalThirdPassSucc = Field()
    finalThirdPassSuccPtn = Field()
    fouled = Field()
    fouledPtn = Field()
    fouls = Field()
    foulsPtn = Field()
    goalSpdSh = Field()
    goalSpdShPtn = Field()
    goals = Field()
    goalsLost = Field()
    goalsLostPtn = Field()
    goalsPtn = Field()
    id = Field()
    interceptions = Field()
    interceptionsPtn = Field()
    keyPasses = Field()
    keyPassesPtn = Field()
    midThirdPass = Field()
    midThirdPassAcc = Field()
    midThirdPassSucc = Field()
    midThirdPassSuccPtn = Field()
    offsideWon = Field()
    offsideWonPtn = Field()
    offsides = Field()
    offsidesPtn = Field()
    passSucc = Field()
    passSuccPtn = Field()
    passes = Field()
    possession = Field()
    possessionPtn = Field()
    rate = Field()
    ratePtn = Field()
    redCards = Field()
    saves = Field()
    savesPtn = Field()
    season = Field()
    seriousError = Field()
    shots = Field()
    shotsConceded = Field()
    shotsConcededPtn = Field()
    shotsOT = Field()
    shotsOTPtn = Field()
    shotsPtn = Field()
    tackles = Field()
    tacklesPtn = Field()
    teamId = Field()
    teamIdWs = Field()
    updateTime = Field()
    yelCards = Field()

class TmatchItem(scrapy.Item):
    collection = 'team_matchstats'









