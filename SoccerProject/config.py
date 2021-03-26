import itertools


class Soccerconfig():
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

    premier_teamID = [262, 12, 19, 15, 13, 264, 16, 4, 8, 10, 3, 14, 507, 269, 263, 1, 2, 20, 7, 11]

    laliga_teamID = [31, 27, 246, 21, 680, 22, 682, 40, 24, 26, 32, 622, 23, 247, 210, 33, 36, 39, 37, 34]

    Italy_teamID = [81, 92, 729, 79, 85, 86, 78, 88, 93, 80, 90, 87, 219, 732, 91, 251, 76, 89, 75, 77]

    German_teamID = [65, 73, 59, 64, 71, 69, 70, 635, 72, 63, 249, 58, 66, 68, 57, 60, 691, 67]

    French_teamID = [106, 114, 113, 111, 842, 109, 108, 1078, 252, 98, 99, 223, 107, 675, 110, 101, 105, 95, 97, 96]

    Brazil_teamID = [204, 193, 187, 190, 2086, 197, 201, 1246, 195, 206, 200, 192, 1870, 628, 202, 629, 188, 199, 191, 198]

    Hollland_teamID = [137, 145, 134, 146, 872, 144, 133, 142, 149, 147, 853, 254, 136, 138, 846, 135, 143, 773]

    Portugal_teamID = [125, 116, 127, 1079, 128, 132, 121, 117, 118, 762, 119, 803, 129, 115, 226, 1920, 124, 122]

    England_teamID = [277, 271, 560, 267, 274, 209, 208, 6, 9, 566, 5, 272, 260, 514, 245, 261, 207, 268, 278, 279, 266, 510, 273, 265]

    Russian_teamID = [162, 155, 166, 1872, 1402, 1930, 165, 152, 163, 153, 159, 151, 156, 161, 1060, 160]

    Turkey_teamID = [286, 1941, 287, 289, 1943, 1822, 756, 285, 893, 1318, 290, 291, 288, 295, 292, 855, 283, 1316, 771, 280, 284]

    Argentina_teamID = [168, 174, 240, 183, 176, 244, 177, 179, 171, 259, 172, 180, 236, 242, 239, 1873, 170, 178, 181, 238, 235, 186, 167, 169]

    China_teamID = [42, 53, 49, 51, 52, 1252, 41, 215, 214, 1257, 45, 1250, 50, 46, 213, 48]

    All_teamID = list(itertools.chain(premier_teamID, laliga_teamID, Italy_teamID, German_teamID, French_teamID,
                                 Brazil_teamID, Hollland_teamID, Portugal_teamID, England_teamID, Russian_teamID,
                                 Turkey_teamID, Argentina_teamID, China_teamID))

    match2id_dict = {
        '英超': 1,
        '西甲': 2,
        '意甲': 5,
        '德甲': 4,
        '法甲': 6,
        '巴甲': 10,
        '荷甲': 8,
        '葡超': 7,
        '英冠': 12,
        '俄超': 9,
        '土超': 13,
        '阿甲': 11,
        '中超': 3
    }

    team2id_dict = {
        #英超
        '富勒姆': 262,
        '阿森纳': 12,
        '水晶宫': 19,
        '南安普顿': 15,
        '利物浦': 13,
        '利兹联': 264,
        '西汉姆联': 16,
        '纽卡斯尔': 4,
        '西布朗维奇': 8,
        '莱斯特城': 10,
        '热刺': 3,
        '埃弗顿': 14,
        '谢菲尔德联': 507,
        '狼队': 269,
        '布莱顿': 263,
        '切尔西': 1,
        '曼联': 2,
        '伯恩利': 20,
        '阿斯顿维拉': 7,
        '曼城': 11,

        # 西甲
        '马德里竞技': 22,
        '皇家马德里': 21,
        '巴塞罗那': 31,
        '塞维利亚': 23,
        '皇家社会': 33,
        '比利亚雷亚尔': 34,
        '皇家贝蒂斯': 210,
        '莱万特': 27,
        '毕尔巴鄂竞技': 24,
        '格拉纳达': 26,
        '塞尔塔': 36,
        '瓦伦西亚': 32,
        '奥萨苏纳': 247,
        '加的斯': 680,
        '赫塔费': 37,
        '埃瓦尔': 40,
        '阿拉维斯': 246,
        '巴拉多利德': 622,
        '埃尔切': 39,
        '韦斯卡': 682,

        #意甲
        '国际米兰': 86,
        'AC米兰': 77,
        '尤文图斯': 75,
        '罗马': 76,
        '亚特兰大': 81,
        '拉齐奥': 78,
        '那不勒斯': 85,
        '萨索罗': 90,
        '维罗纳': 93,
        '桑普多利亚': 89,
        '热那亚': 80,
        '博洛尼亚': 219,
        '乌迪内斯': 88,
        '佛罗伦萨': 87,
        '贝内文托': 729,
        '斯佩齐亚': 732,
        '都灵': 79,
        '卡利亚里': 92,
        '帕尔马': 91,
        '克罗托内': 251,

        #德甲
        '拜仁慕尼黑': 57,
        '莱比锡红牛': 249,
        '沃尔夫斯堡': 67,
        '法兰克福': 70,
        '勒沃库森': 59,
        '多特蒙德': 66,
        '柏林联盟': 635,
        '门兴': 60,
        '弗赖堡': 64,
        '斯图加特': 69,
        '霍芬海姆': 68,
        '云达不莱梅': 72,
        '奥格斯堡': 65,
        '科隆': 73,
        '柏林赫塔': 71,
        '比勒费尔德': 691,
        '美因茨': 63,
        '沙尔克04': 58,

        #法甲
        '里尔': 107,
        '里昂': 106,
        '巴黎圣日耳曼': 95,
        '摩纳哥': 105,
        '梅斯': 113,
        '朗斯': 114,
        '马赛': 96,
        '雷恩': 98,
        '蒙彼利埃': 110,
        '昂热': 223,
        '波尔多': 108,
        '尼斯': 99,
        '布雷斯特': 675,
        '兰斯': 111,
        '圣埃蒂安': 97,
        '斯特拉斯堡': 1078,
        '尼姆': 842,
        '南特': 101,
        '洛里昂': 109,
        '第戎': 252,

        #巴甲
        '弗拉门戈': 200,
        '巴西国际': 192,
        '米内罗竞技': 197,
        '圣保罗': 187,
        '弗鲁米嫩塞': 199,
        '格雷米奥': 190,
        '帕尔梅拉斯': 201,
        '桑托斯': 198,
        '巴拉纳竞技': 204,
        '布拉甘蒂诺红牛': 2086,
        '塞阿拉竞技': 1246,
        '科林蒂安': 188,
        '戈亚尼恩斯竞技': 629,
        '巴伊亚': 193,
        '累西腓体育': 195,
        '福塔雷萨': 1870,
        '瓦斯科达伽马': 628,
        '戈亚斯': 206,
        '科里蒂巴': 202,
        '博塔弗戈': 191,

        #荷甲
        '阿贾克斯': 133,
        '埃因霍温': 142,
        '阿尔克马尔': 144,
        '费耶诺德': 143,
        '维特斯': 135,
        '格罗宁根': 137,
        '乌德勒支': 136,
        '特温特': 134,
        '锡塔德福图纳': 872,
        '海伦芬': 145,
        '赫拉克勒斯': 138,
        '兹沃勒': 146,
        '鹿特丹斯巴达': 254,
        '瓦尔维克': 773,
        '芬洛': 846,
        '威廉二世': 149,
        '海牙': 147,
        '埃门': 853,

        #葡甲
        '葡萄牙体育': 116,
        '波尔图': 115,
        '布拉加': 125,
        '本菲卡': 124,
        '费雷拉': 121,
        '吉马良斯': 128,
        '圣克拉拉': 803,
        '摩里伦斯': 129,
        '里奥阿维': 117,
        '比兰尼塞斯': 122,
        '国民队': 118,
        '通德拉': 226,
        '波尔蒂芒': 1079,
        '吉尔维森特': 119,
        '法鲁人体育': 1920,
        '博阿维斯塔': 132,
        '费马利卡奥': 762,
        '马里迪莫': 127,

        #英冠
        '诺维奇': 209,
        '布伦特福德': 271,
        '沃特福德': 207,
        '斯旺西': 5,
        '伯恩茅斯': 208,
        '雷丁': 265,
        '卡迪夫': 268,
        '巴恩斯利': 279,
        '米德尔斯堡': 245,
        '斯托克城': 6,
        '米尔沃尔': 514,
        '布里斯托尔城': 272,
        '女王公园巡游者': 9,
        '诺丁汉森林': 266,
        '普雷斯顿': 274,
        '布莱克本': 267,
        '德比郡': 260,
        '卢顿': 560,
        '哈德斯菲尔德': 278,
        '考文垂': 566,
        '伯明翰': 273,
        '罗瑟汉姆联': 277,
        '谢周三': 261,
        '韦康比': 510,

        #俄超
        '泽尼特': 151,
        '莫斯科中央陆军': 159,
        '莫斯科斯巴达': 153,
        '索契FC': 1872,
        '罗斯托夫': 163,
        '莫斯科迪纳摩': 152,
        '克拉斯诺达尔': 162,
        '莫斯科火车头': 160,
        '希姆基': 1402,
        '喀山红宝石': 161,
        '艾卡马特': 155,
        '乌拉尔': 156,
        '伏尔加格勒转子': 1930,
        '图拉兵工厂': 166,
        '乌法': 165,
        '坦波夫': 1060,

        #土超
        '加拉塔萨雷': 287,
        '贝西克塔斯': 284,
        '费内巴切': 280,
        '特拉布宗体育': 283,
        '哈塔伊体育': 1943,
        '阿拉尼亚体育': 292,
        '法蒂赫卡拉古鲁克': 1941,
        '加济安泰普FK': 756,
        '安塔利亚体育': 288,
        '哥兹塔比': 855,
        '锡瓦斯体育': 771,
        '科尼亚体育': 291,
        '马拉蒂亚体育': 893,
        '卡斯帕萨': 285,
        '里泽体育': 289,
        '开塞利体育': 295,
        '埃尔祖鲁姆': 1822,
        '巴萨克赛尔': 286,
        '代尼兹利体育': 1316,
        '根克勒比利吉': 290,
        '安卡拉古库': 1318,

        #阿甲
        '博卡青年': 168,
        '河床': 177,
        '萨斯菲尔德': 169,
        '竞技': 179,
        '阿根廷青年人': 236,
        '防卫者': 176,
        '拉努斯': 170,
        '圣洛伦索': 167,
        '罗萨里奥中央': 186,
        '纽维尔老男孩': 178,
        '萨兰迪兵工厂': 180,
        '塔莱雷斯竞技': 259,
        '拉普拉塔大学生': 171,
        '独立': 181,
        '图库曼竞技': 239,
        '圣菲联合': 238,
        '班菲尔德': 183,
        '科尔多瓦中央': 1873,
        '拉普拉塔体操': 172,
        '帕特洛纳托': 244,
        '飓风竞技': 235,
        '阿尔多希维': 242,
        '科隆竞技': 240,
        '戈多伊克鲁斯': 174,

        #中超
        '广州恒大': 41,
        '江苏苏宁': 53,
        '山东鲁能': 49,
        '上海绿地申花': 50,
        '深圳佳兆业': 1250,
        '广州富力': 51,
        '大连人': 52,
        '河南建业': 48,
        '上海上港': 45,
        '北京国安': 42,
        '重庆力帆': 215,
        '河北华夏幸福': 213,
        '石家庄永昌': 214,
        '武汉卓尔': 1252,
        '青岛黄海青港': 1257,
        '天津泰达': 46,
    }

    id2team_dict = dict(zip(team2id_dict.values(), team2id_dict.keys()))

    team_field_map = {
            'aerialWon': 'aerialWon',
            'aerialWonPtn': 'aerialWonPtn',
            'apps': 'apps',
            'assists': 'assists',
            'assistsPtn': 'assistsPtn',
            'ballRecovery': 'ballRecovery',
            'ballRecoveryPtn': 'ballRecoveryPtn',
            'bigChanceCreated': 'bigChanceCreated',
            'bigChanceCreatedPtn': 'bigChanceCreatedPtn',
            'bigChanceMissed': 'bigChanceMissed',
            'bigChanceMissedPtn': 'bigChanceMissedPtn',
            'bigChanceScored': 'bigChanceScored',
            'bigChanceScoredPtn': 'bigChanceScoredPtn',
            'bigChanceSucc': 'bigChanceSucc',
            'bigChanceSuccPtn': 'bigChanceSuccPtn',
            'cardPtn': 'cardPtn',
            'clears': 'clears',
            'clearsPtn': 'clearsPtn',
            'competitionId': 'competitionId',
            'competitionIdWs': 'competitionIdWs',
            'createTime': 'createTime',
            'defensiveThirdPass': 'defensiveThirdPass',
            'defensiveThirdPassAcc': 'defensiveThirdPassAcc',
            'defensiveThirdPassSucc': 'defensiveThirdPassSucc',
            'defensiveThirdPassSuccPtn': 'defensiveThirdPassSuccPtn',
            'dribbles': 'dribbles',
            'dribblesPtn': 'dribblesPtn',
            'errorsSum': 'errorsSum',
            'errorsSumPtn': 'errorsSumPtn',
            'fatalError': 'fatalError',
            'finalThirdPass': 'finalThirdPass',
            'finalThirdPassAcc': 'finalThirdPassAcc',
            'finalThirdPassSucc': 'finalThirdPassSucc',
            'finalThirdPassSuccPtn': 'finalThirdPassSuccPtn',
            'fouled': 'fouled',
            'fouledPtn': 'fouledPtn',
            'fouls': 'fouls',
            'foulsPtn': 'foulsPtn',
            'goalSpdSh': 'goalSpdSh',
            'goalSpdShPtn': 'goalSpdShPtn',
            'goals': 'goals',
            'goalsLost': 'goalsLost',
            'goalsLostPtn': 'goalsLostPtn',
            'goalsPtn': 'goalsPtn',
            'id': 'id',
            'interceptions': 'interceptions',
            'interceptionsPtn': 'interceptionsPtn',
            'keyPasses': 'keyPasses',
            'keyPassesPtn': 'keyPassesPtn',
            'midThirdPass': 'midThirdPass',
            'midThirdPassAcc': 'midThirdPassAcc',
            'midThirdPassSucc': 'midThirdPassSucc',
            'midThirdPassSuccPtn': 'midThirdPassSuccPtn',
            'offsideWon': 'offsideWon',
            'offsideWonPtn': 'offsideWonPtn',
            'offsides': 'offsides',
            'offsidesPtn': 'offsidesPtn',
            'passSucc': 'passSucc',
            'passSuccPtn': 'passSuccPtn',
            'passes': 'passes',
            'possession': 'possession',
            'possessionPtn': 'possessionPtn',
            'rate': 'rate',
            'ratePtn': 'ratePtn',
            'redCards': 'redCards',
            'saves': 'saves',
            'savesPtn': 'savesPtn',
            'season': 'season',
            'seriousError': 'seriousError',
            'shots': 'shots',
            'shotsConceded': 'shotsConceded',
            'shotsConcededPtn': 'shotsConcededPtn',
            'shotsOT': 'shotsOT',
            'shotsOTPtn': 'shotsOTPtn',
            'shotsPtn': 'shotsPtn',
            'tackles': 'tackles',
            'tacklesPtn': 'tacklesPtn',
            'teamId': 'teamId',
            'teamIdWs': 'teamIdWs',
            'updateTime': 'updateTime',
            'yelCards': 'yelCards'
    }


    def judgeleague(self, id):
        if id in self.premier_teamID:
            return '英超'
        elif id in self.laliga_teamID:
            return '西甲'
        elif id in self.Italy_teamID:
            return '意甲'
        elif id in self.German_teamID:
            return '德甲'
        elif id in self.French_teamID:
            return '法甲'
        elif id in self.Brazil_teamID:
            return '巴甲'
        elif id in self.Hollland_teamID:
            return '荷甲'
        elif id in self.Portugal_teamID:
            return '葡超'
        elif id in self.England_teamID:
            return '英冠'
        elif id in self.Russian_teamID:
            return '俄超'
        elif id in self.Turkey_teamID:
            return '土超'
        elif id in self.Argentina_teamID:
            return '阿甲'
        elif id in self.China_teamID:
            return '中超'


