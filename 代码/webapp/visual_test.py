import pandas as pd

import json

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Map,Bar, Tab, Pie, Line,Timeline,Page,Geo,Scatter


df = pd.read_csv('/home/SHIRKINGLIANG/mysite/All.csv',encoding="gbk")
regions_available_loaded = list(df["指标"].dropna().unique())

BQ = df[df['指标']== "BaseQuantity" ]
C = df[df['指标']== "Collection" ]
V = df[df['指标']== "Visitors" ]
P = df[df['指标']== "Practitioner" ]
PCF = df[df['指标']== "PublicCulturalFinance" ]
CSMF = df[df['指标']== "CultureSportsMediaFinance" ]
GDP = df[df['指标']== "GDP" ]
P2 = df[df['指标']== "Population" ]
BC = df[df['指标']== "BookCollection" ]
NOLI = df[df['指标']== "NumberOfLibraryInstitutions" ]
DIPC = df[df['指标']== "DisposableIncomePerCapita" ]


DQ = BQ['地区']
DQ = list(DQ)
DQ1 = [dq.replace('市', '') for dq in DQ]
DQ2 = [dq.replace('省', '') for dq in DQ1]
DQ3 = [dq.replace('自治区', '') for dq in DQ2]
DQ4 = [dq.replace('壮族', '') for dq in DQ3]
DQ5 = [dq.replace('回族', '') for dq in DQ4]
DQ_end = [dq.replace('维吾尔', '') for dq in DQ5]


BQ2018 = list(BQ['2018年'])
BQ2017 = list(BQ['2017年'])
BQ2016 = list(BQ['2016年'])
BQ2015 = list(BQ['2015年'])
BQ2014 = list(BQ['2014年'])
BQ2013 = list(BQ['2013年'])
BQ2012 = list(BQ['2012年'])
BQ2011 = list(BQ['2011年'])
BQ2010 = list(BQ['2010年'])


x = [list(z) for z in zip(DQ_end,BQ2018)]


DQ = BQ['地区']
DQ = list(DQ)

v2018 = V['2018年']
v2018 = list(v2018)

p2018 = P['2018年']
p2018 = list(p2018)

coll2018 = C['2018年']
coll2018 = list(coll2018)

coll2017 = C['2017年']
coll2017 = list(coll2017)

coll2016 = C['2016年']
coll2016 = list(coll2016)

coll2015 = C['2015年']
coll2015 = list(coll2015)


y1 = [list(z) for z in zip(DQ_end,coll2018)]

y2 = [list(z) for z in zip(DQ_end,coll2017)]

y3 = [list(z) for z in zip(DQ_end,coll2016)]

y4 = [list(z) for z in zip(DQ_end,coll2015)]

f12018 = list(PCF["2018年"])
f22018 = list(CSMF["2018年"])



bx =[list(z) for z in zip(DQ_end,BC["2018年"])]


#  BaseQuantity

def geo_1() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china",
                    itemstyle_opts=opts.ItemStyleOpts(color="#003557", border_color="#00C4FA"),
                   )
        .add("博物馆机构数（个）",x)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=517,min_ = 7),
            title_opts=opts.TitleOpts(title="全国博物馆机构数（个）"),
        )
    )
    return c

def line_smooth() -> Line:
    c = (
        Line()
        .add_xaxis(DQ)
        .add_yaxis("2010", BQ2010, is_smooth=True)
        .add_yaxis("2011", BQ2011, is_smooth=True)
        .add_yaxis("2012", BQ2012, is_smooth=True)
        .add_yaxis("2013", BQ2013, is_smooth=True)
        .add_yaxis("2014", BQ2014, is_smooth=True)
        .add_yaxis("2015", BQ2015, is_smooth=True)
        .add_yaxis("2016", BQ2016, is_smooth=True)
        .add_yaxis("2017", BQ2017, is_smooth=True)
        .add_yaxis("2018", BQ2018, is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="近八年各地区博物馆机构数变化情况"),
                        datazoom_opts=[opts.DataZoomOpts(),opts.DataZoomOpts(orient="vertical"), opts.DataZoomOpts(type_="inside")],
                        )
    )
    return c



# Collection

def map_visualmap() -> Map:
    c = (
        Map()
        .add("藏品量（个/套）",y1, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国各地博物馆藏品量分布图"),
            visualmap_opts=opts.VisualMapOpts(max_=4027, is_piecewise=True),
        )
    )
    return c




# Practitioner

def bar3() -> Bar:
    c = (
        Bar(
            init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts(
                    animation_delay=1000, animation_easing="elasticOut"
                )
            )
        )
        .add_xaxis(DQ)
        .add_yaxis("从业人员", p2018)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2018年各地区从业人员数量对比")
        )
    )
    return c


def practitioner_bar() -> Bar:
    c = (
        Bar()
        .add_xaxis(DQ)
        .add_yaxis("机构数（个）", BQ2018)
        .add_yaxis("收藏品（千套）", coll2018)
        .add_yaxis("参观者（万人次）", v2018)
        .add_yaxis("从业人员（人）", p2018)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="博物馆相关信息图"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=True),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


# Visitor

def bar_base_with_animation() -> Bar:
    c = (
        Bar(
            init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts(
                    animation_delay=1000, animation_easing="elasticOut"
                )
            )
        )
        .add_xaxis(DQ)
        .add_yaxis("参观人数（万人次）", v2018)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2018年各地区参观人员数量对比", subtitle="")
        )
    )
    return c


def visitor_bar2() -> Bar:
    c = (
        Bar()
        .add_xaxis(DQ)
        .add_yaxis("机构数（个）", BQ2018)
        .add_yaxis("收藏品（千套）", coll2018)
        .add_yaxis("参观者（万人次）", v2018)
        .add_yaxis("从业人员（人）", p2018)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="博物馆相关信息图"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=True),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


# GDP  Population DisposableIncomePerCapita

def GDP_line() -> Line:
    c = (
        Line()
        .add_xaxis(DQ)
        .add_yaxis(
            "地区生产总值(亿元)",
           GDP["2018年"],
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .add_yaxis(
            "年末常住人口(万人)",
            P2["2018年"],
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2018年GDP与人口"),
            datazoom_opts=[opts.DataZoomOpts(),
            opts.DataZoomOpts(orient="vertical"),
            opts.DataZoomOpts(type_="inside")],
        )
    )
    return c



#人均可支配收入

def DIC_scatter() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(DQ)
        .add_yaxis("2018年人均可支配收入（十元）", list(DIPC["2018年"]))
        .add_yaxis("博物馆机构数", BQ2018)
        .set_global_opts(title_opts=opts.TitleOpts(title="2018年全国各地可支配收入展示"),
                         datazoom_opts=[opts.DataZoomOpts(),
                        opts.DataZoomOpts(orient="vertical"),
                        opts.DataZoomOpts(type_="inside")],)
        )
    return c

def compare_bar3() -> Bar:
    c = (
        Bar()
        .add_xaxis(DQ)
        .add_yaxis("机构数（个）", BQ2018)
        .add_yaxis("收藏品（千套）", coll2018)
        .add_yaxis("参观者（万人次）", v2018)
        .add_yaxis("从业人员（人）", p2018)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="博物馆相关信息图"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=True),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


# BookCollection NumberOfLibraryInstitution

def library_and_museum_distribute() -> Pie:
    v = DQ
    c = (
        Pie()
        .add(
            "博物馆",
            [list(z) for z in zip(v,BQ2018)],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "图书馆",
            [list(z) for z in zip(v, NOLI["2018年"])],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    return c

#地图分布状况

def book_distribute_map() -> Map:
    c = (
        Map()
        .add("书籍分布图（万册）", bx, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2018年图书馆书籍收藏分布状况及与图书馆对比"),
            visualmap_opts=opts.VisualMapOpts(max_=9547.57,min_=221.06 ,is_piecewise=True),
        )
    )
    return c


# PublicCulturalFinance CultureSportsMediaFinance

def bar_stack0() -> Bar:
    c = (
        Bar()
        .add_xaxis(DQ)
        .add_yaxis("PublicCulturalFinance地方财政一般公共服务支出(亿元)", f12018, stack="stack1")
        .add_yaxis("CultureSportsMediaFinance地方财政文化体育与传媒支出(亿元)",f22018, stack="stack1")
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                    opts.MarkPointItem(type_="average", name="平均值"),
                ]
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="财政",subtitle="2018年中国各地区博物馆相关财政支出对比"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            toolbox_opts=opts.ToolboxOpts(),
            )
    )
    return c

def museum_related_info_bar() -> Bar:
    c = (
        Bar()
        .add_xaxis(DQ)
        .add_yaxis("机构数（个）", BQ2018)
        .add_yaxis("收藏品（千套）", coll2018)
        .add_yaxis("参观者（万人次）", v2018)
        .add_yaxis("从业人员（人）", p2018)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="博物馆相关信息图"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=True),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    return c


