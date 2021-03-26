from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.faker import Faker
import json


def ShowGoal(team_name, team_shot, team_goal):
    c = (
        Scatter(opts.InitOpts(
        width="2000px",
        height="600px",
        renderer= "svg",
        theme= "chalk"))
            .add_xaxis(team_name)
            .add_yaxis("场均射门", team_shot)
            .add_yaxis("总进球", team_goal)
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(type_='category'),
            legend_opts=opts.LegendOpts(is_show=True),
            title_opts=opts.TitleOpts(title="英超"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=0, min_=1500),
        )
            .render("ShowGoal.html")
    )


if __name__ == '__main__':
    with open("spiders/a.json", encoding='utf-8', errors='ignore') as json_data:
        data = json.load(json_data, strict=False)

    team_name = list()
    team_shot = list()
    team_goal = list()
    for team in data:
        team_name.append(team['name'])
        team_shot.append(team['shots'])
        team_goal.append(team['goals'])

    team_stats = zip(team_goal, team_name, team_shot)
    team_stats_sorted = list(zip(*sorted(team_stats)))

    team_goal = team_stats_sorted[0]
    team_name = team_stats_sorted[1]
    team_shot = team_stats_sorted[2]
    ShowGoal(team_name, team_shot, team_goal)