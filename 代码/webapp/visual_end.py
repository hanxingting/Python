from flask import Flask, render_template, request
import pandas as pd
import json
from visual_test import geo_1, line_smooth,map_visualmap,bar3, practitioner_bar,bar_base_with_animation, visitor_bar2,GDP_line, DIC_scatter, compare_bar3,book_distribute_map,library_and_museum_distribute,bar_stack0, museum_related_info_bar
from pyecharts.charts import Page
import plotly as py
import numpy as np

from jinja2 import Markup

app = Flask(__name__)

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



def plot_all(kw):
    page = Page(layout=Page.SimplePageLayout)
    kw_map = {"BaseQuantity": [geo_1, line_smooth],
              "Collection": [map_visualmap],
              "Practitioner": [bar3, practitioner_bar],
              "Visitors": [bar_base_with_animation, visitor_bar2],
              "GDP": [GDP_line, DIC_scatter, compare_bar3],
              "Population": [GDP_line, DIC_scatter, compare_bar3],
              "BookCollection": [book_distribute_map,library_and_museum_distribute],
              "PublicCulturalFinance": [bar_stack0, museum_related_info_bar],
              "CultureSportsMediaFinance": [bar_stack0, museum_related_info_bar],
              "NumberOfLibraryInstitutions": [book_distribute_map,library_and_museum_distribute],
              "DisposableIncomePerCapita": [GDP_line, DIC_scatter, compare_bar3]
             }
    for f in kw_map[kw]:
        page.add(f())
    return page.render_embed()


plot_desc = {"BaseQuantity": " 从这两页的数据我们可以看出近八年间，山东、河南、浙江、陕西、四川等地的博物馆机构数激增。\
             尤其是山东省从2010年的114个狂涨到2018年的517个。从地图上看，2018年，我国博物馆机构主要集中于黄河中下游、长江下游地区。\
             和中国文明发展的方向基本一致，历史发展比较久远且兴盛的地区能够出现更多博物馆机构。\
             同时我们可以看见马太效应在这其中也有一定的显现，原本博物馆数量较多的地区博物馆增长量要比原本博物馆数量较少的地区要多很多，山东就是其中一个例子。",
          "Collection": "我国主要的博物馆收藏品分布在山东、陕西、四川三个大省，并明显呈现出东多西少的区域分布状况。这和我们对博物馆的原有印象也基本一致。\
          但是经济发达的地区不一定是博物馆发展最多的，当然，也一定的存在有博物馆的资源集中化的现象。就像北京，绝大多数的资源都集中到了故宫博物馆以及国家博物馆中。" ,
          "Practitioner": "陕西作为旅游胜地，博物馆规模大，从业人员多是可想而知的。其次，江苏地区有大量参观者进入，也容易催生一大批从业人员。\
          但从这里我们可以发现，从业人员的多寡与该地区机构数的多少并不是相互呼应的。同时，和博物馆的参观人数对比也可以看见两者的峰值都出现在不同的位置。\
          这和各地区博物馆的知名度、旅游人数、单个博物馆的机构大小也有一定的关系。",
          "Visitors": "结合我们之前学到的地理知识，我们观察到一个现象：在经济发达地区附近的比较郊区的地区会有比较多的参观者，尤其是观察长江三角洲地区。\
                      另外，历史文化底蕴丰富的陕西也是参观者众多的地区。兵马俑、古长安皆在此地。",
          "GDP": "结合我们之前学到的地理知识，我们观察到一个现象：在经济发达地区附近的比较郊区的地区会有比较多的参观者，尤其是观察长江三角洲地区。\
                  另外，历史文化底蕴丰富的陕西也是参观者众多的地区。兵马俑、古长安皆在此地。同时我们也可以知道，经济对于博物馆而言影响并没有我们想象中的大，\
                  不能完全成为决定性影响。博物馆的发展是一个天时地利人和的结果，该地区原有的历史文化底蕴、时代经历在这其中有着很重要的地位。",
          "Population": "结合我们之前学到的地理知识，我们观察到一个现象：在经济发达地区附近的比较郊区的地区会有比较多的参观者，尤其是观察长江三角洲地区。\
                  另外，历史文化底蕴丰富的陕西也是参观者众多的地区。兵马俑、古长安皆在此地。",
          "BookCollection": "经对比可以看见，书籍收藏分布与博物馆收藏分布之间还是有不少的重合点。可以看见，江苏、山东、四川、河南、上海等地对于公共文化服务的重视程度是比较高的。",
          "PublicCulturalFinance": "从图中可以看出 广东省在对于公共服务及文化输出的财政投入最大，博物馆机构数最多的山东省的投入反倒没有那么突出。\
                                    从这两个图的对比我们可以充分明白，经济投入与博物馆机构建设数量之间相关性并不强，但投入较少的海南、青海、宁夏等地博物馆机构数确实比较少，这里倒是显示出一致性。",
          "CultureSportsMediaFinance": "从图中可以看出 广东省在对于公共服务及文化输出的财政投入最大，博物馆机构数最多的山东省的投入反倒没有那么突出。\
                                        从这两个图的对比我们可以充分明白，经济投入与博物馆机构建设数量之间相关性并不强，但投入较少的海南、青海、宁夏等地博物馆机构数确实比较少。",
          "NumberOfLibraryInstitutions": "经对比可以看见，书籍收藏分布与博物馆收藏分布之间还是有不少的重合点。可以看见，江苏、山东、四川、上海等地对于公共文化服务的重视程度是比较高的。",
          "DisposableIncomePerCapita": "结合我们之前学到的地理知识，我们观察到一个现象：在经济发达地区附近的比较郊区的地区会有比较多的参观者，尤其是观察长江三角洲地区。\
                  另外，历史文化底蕴丰富的陕西也是参观者众多的地区。兵马俑、古长安皆在此地。人们可支配收入的提升也会提高人们对于精神文化的追求，提高人们对于公共文化服务的重视程度。"
         }

@app.route('/',methods=['GET'])
def hu_run_2019():

    data_str = df.to_html()


    regions_available = regions_available_loaded
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=regions_available)



@app.route('/first',methods=['POST'])
def hu_run_select() -> 'html':



    the_region = request.form["the_region_selected"]
    print(the_region)

    dfs = df.query("指标=='{}'".format(the_region))


    data_str = dfs.to_html()


    regions_available =  regions_available_loaded
    return render_template('results2.html',
                           the_plot_all=plot_all(the_region),
                           echart_desc=plot_desc[the_region],
                           the_res=data_str,
                           the_select_region=regions_available,
                           )

if __name__ == '__main__':
    app.run(debug=True)
