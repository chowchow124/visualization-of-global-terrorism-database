# 定义函数HeaderInfo()，该函数返回一个html.Div元素
# 该元素包含h1元素和p元素，即标题和描述

# 底部内边距为 30 像素
# 顶部外边距为 -50 像素

from dash import html
from api import year_min,year_max

def HeaderInfo():
    return html.Div(
        [
            html.H4(
                html.A(
                    'Global Terrorism Database', 
                    href='https://www.start.umd.edu/gtd/contact/download?t=2b9bc31e4b2011ef91260e5194896103',
                    target='_blank',
                    style={
                        'text-decoration': 'underline',  # 使文本有下划线
                        'color': 'white',  # 设置文本颜色为黑色
                    })
            ),
            html.P(f'{year_min}-{year_max}')
        ],style={'padding-bottom': '10px', 'margin-top': '0px'}  
    )
