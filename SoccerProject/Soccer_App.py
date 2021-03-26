import streamlit as st
import numpy as np
import pandas as pd
import time
import codecs
from config import Soccerconfig
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Pie
from pyecharts.charts import Scatter
from pyecharts.commons.utils import JsCode
from pyecharts.globals import RenderType
from pyecharts.globals import ThemeType


def get_stats(df, type):
    df_temp = pd.DataFrame()
    df_temp = df
    if type == 0:
        df_temp['possession'] = df_temp['possession'] * 100
        df_temp['passSucc'] = df_temp['passSucc'] * 100
        return pd.DataFrame(df_temp.round(2), columns=['possession', 'passSucc',
                                                       'keyPasses', 'bigChanceCreated',
                                                       'aerialWon', 'rate']).values.tolist()[0]
    if type == 1:
        df_temp['bigChanceSucc'] = df_temp['bigChanceSucc'] * 100
        return pd.DataFrame(df_temp.round(2), columns=['goals', 'shots',
                                                       'shotsOT', 'bigChanceSucc',
                                                       'dribbles', 'fouled']).values.tolist()[0]
    if type == 2:
        return pd.DataFrame(df_temp.round(2), columns=['goalsLost', 'shotsConceded',
                                                       'tackles', 'interceptions',
                                                       'clears', 'fouls', 'errorsSum']).values.tolist()[0]
    if type == 3:
        df_temp['finalThirdPassSucc'] = df_temp['finalThirdPassSucc'] * 100
        return pd.DataFrame(df_temp.round(2), columns=['assists', 'bigChanceCreated',
                                                       'keyPasses', 'finalThirdPassSucc',
                                                       'ballRecovery']).values.tolist()[0]

    return None


if __name__ == '__main__':
    st.title('阿猿战术板')
    Config = Soccerconfig

    df = pd.read_json("spiders/a.json", encoding="utf-8", orient='records')

    option1_l = st.sidebar.selectbox(
        '输入主队所属联赛名称',
        ['英超', '西甲', '意甲', '德甲', '法甲',
         '巴甲', '荷甲', '葡超', '英冠', '俄超',
         '土超', '阿甲', '中超']
    )

    if option1_l == '英超':
        aa = df.loc[df['league_name'] == '英超']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '西甲':
        aa = df.loc[df['league_name'] == '西甲']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '意甲':
        aa = df.loc[df['league_name'] == '意甲']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '德甲':
        aa = df.loc[df['league_name'] == '德甲']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )

    elif option1_l == '法甲':
        aa = df.loc[df['league_name'] == '法甲']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )

    elif option1_l == '巴甲':
        aa = df.loc[df['league_name'] == '巴甲']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '荷甲':
        aa = df.loc[df['league_name'] == '荷甲']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '葡超':
        aa = df.loc[df['league_name'] == '葡超']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '英冠':
        aa = df.loc[df['league_name'] == '英冠']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '俄超':
        aa = df.loc[df['league_name'] == '俄超']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '土超':
        aa = df.loc[df['league_name'] == '土超']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '阿甲':
        aa = df.loc[df['league_name'] == '阿甲']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )
    elif option1_l == '中超':
        aa = df.loc[df['league_name'] == '中超']
        aa = list(aa['name'])
        option1 = st.sidebar.selectbox(
            '输入主队队名',
            aa
        )

    option2_l = st.sidebar.selectbox(
        '输入客队所属联赛名称',
        ['英超', '西甲', '意甲', '德甲', '法甲',
         '巴甲', '荷甲', '葡超', '英冠', '俄超',
         '土超', '阿甲', '中超']
    )

    if option2_l == '英超':
        aa = df.loc[df['league_name'] == '英超']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '西甲':
        aa = df.loc[df['league_name'] == '西甲']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '意甲':
        aa = df.loc[df['league_name'] == '意甲']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '德甲':
        aa = df.loc[df['league_name'] == '德甲']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )

    elif option2_l == '法甲':
        aa = df.loc[df['league_name'] == '法甲']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )

    elif option2_l == '巴甲':
        aa = df.loc[df['league_name'] == '巴甲']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '荷甲':
        aa = df.loc[df['league_name'] == '荷甲']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '葡超':
        aa = df.loc[df['league_name'] == '葡超']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '英冠':
        aa = df.loc[df['league_name'] == '英冠']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '俄超':
        aa = df.loc[df['league_name'] == '俄超']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '土超':
        aa = df.loc[df['league_name'] == '土超']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '阿甲':
        aa = df.loc[df['league_name'] == '阿甲']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )
    elif option2_l == '中超':
        aa = df.loc[df['league_name'] == '中超']
        aa = list(aa['name'])
        option2 = st.sidebar.selectbox(
            '输入客队队名',
            aa
        )

    option3 = st.sidebar.selectbox(
        '使用模型',
        ['Gradient Boosting Decision Tree', 'Deep Forest', 'Deep Neural Network', 'Model Boosting']
    )

    team1 = df.loc[df['name'] == option1]
    team2 = df.loc[df['name'] == option2]

    st.markdown('正在分析 **' + option1 + '** 与 **' + option2 + '** 的比赛')
    c = (
        Bar()
            .add_xaxis(
            [
                "控球率",
                "传球成功率",
                "场均关键传球",
                "绝佳机会",
                "场均争顶成功",
                "评分",
            ]
        )
            .add_yaxis(option1, get_stats(team1, 0), color= '#749f83')
            .add_yaxis(option2, get_stats(team2, 0), color= '#d48265')
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10)),
            title_opts=opts.TitleOpts(title="球队概况"),

        )
    )
    st_pyecharts(c)

    MoreStats = st.multiselect('Select', ['进攻', '防守', '组织'])
    if '进攻' in MoreStats:
        c = (
            Bar()
                .add_xaxis(
                [
                    "进球",
                    "场均射门",
                    "场均射正",
                    "把握机会能力",
                    "场均过人",
                    "场均被侵犯",
                ]
            )
                .add_yaxis(option1, get_stats(team1, 1))
                .add_yaxis(option2, get_stats(team2, 1))
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10)),
                title_opts=opts.TitleOpts(title="球队进攻对比"),
            )
        )
        st_pyecharts(c)

    if '防守' in MoreStats:
        c = (
            Bar()
                .add_xaxis(
                [
                    "失球",
                    "场均被射门",
                    "场均抢断",
                    "场均拦截",
                    "场均解围",
                    "场均犯规",
                    "致命失误"
                ]
            )
                .add_yaxis(option1, get_stats(team1, 2))
                .add_yaxis(option2, get_stats(team2, 2))
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10)),
                title_opts=opts.TitleOpts(title="球队防守对比"),
            )
        )
        st_pyecharts(c)

    if '组织' in MoreStats:
        c = (
            Bar()
                .add_xaxis(
                [
                    "助攻",
                    "创造绝佳机会",
                    "场均关键传球",
                    "前场传球成功率",
                    "场均夺回球权"
                ]
            )
                .add_yaxis(option1, get_stats(team1, 3))
                .add_yaxis(option2, get_stats(team2, 3))
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10)),
                title_opts=opts.TitleOpts(title="球队组织对比"),
            )
        )
        st_pyecharts(c)

    if st.button('开始预测比赛'):
        '⏳⏳⏳...'

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Iteration {i + 1}')
            bar.progress(i + 1)
            time.sleep(0.1)

        '...预测结束，输出比赛结果'
        x_data = ['主队胜', '平局', '客队胜']
        y_data = [24.29, 53.78, 21.93]
        assert sum(y_data) == 100.
        data_pair = [list(z) for z in zip(x_data, y_data)]

        result = (
            Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
                .add(
                "Percentage",
                data_pair,
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter=" {b|{b}: } {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0, 0],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="比赛预测结果"))
        )
        st_pyecharts(result)

    st.image('./Resources/ape_board_dark.jpg')
