from dash import html
from dash import html,dcc,Input,Output
from app import app
import plotly.graph_objects as go
from api import get_bar_data
import plotly.express as px


# 该函数返回一个包含 html.Div元素的布局，id为stack-content，用于存放动态更新的图表内容
def StackBarLineInfo():
    return html.Div(
        [
            html.Div(id='stack-content')
        ]
    )

# 根据用户在前端选择的区域、国家和年份范围动态更新图表内
@app.callback(
    Output('stack-content','children'),
    [Input('Region','value'),Input('Country','value'),Input('Span-year','value')]
)
def update(region,country,span_year):

    death,wounded,attackCount = get_bar_data(region,country,span_year)
    span_year_ls = list(range(span_year[0],span_year[1]+1))
    
    fig = go.Figure(
        [
            # 两个堆叠柱状图，一个折线图组成的复合图表
            go.Bar(x=span_year_ls,y=death,name='Death'),
            go.Bar(x=span_year_ls,y=wounded,name='Injured'),
            go.Scatter(mode='markers + lines',x=span_year_ls,y=attackCount,name='AttackCount')
        ]
    )
    fig.update_layout(
            barmode = 'stack',
            titlefont = {'color':'white','size':20},
            font = {'family':'sans-serif','color':'white','size':12},
            hovermode = 'closest',
            paper_bgcolor = '#070707',
            plot_bgcolor = '#070707',
            legend = {'orientation':'h','bgcolor':'#070707','xanchor':'center','x': 0.5, 'y': -0.2},
            margin = {'r':0,'l':60,'b':100,'t':20},

            xaxis = {'title':'<b>Year</b>','color':'white','showline':True,'showgrid':True,'tick0':0,'dtick':1,'gridcolor':'#010915',
                    'showticklabels':True,'linecolor':'white','linewidth':1,'ticks':'outside','tickfont':{'family':'sans-serif','color':'white','size':12}
                    },
            yaxis = {'title':'<b>Death</b>','color':'white','showline':True,'showgrid':True,'gridcolor':'#010915',
                    'showticklabels':True,'linecolor':'white','linewidth':1,'ticks':'outside','tickfont':{'family':'sans-serif','color':'white','size':12}
                    }
    )
    return [
        html.P(f'Death, Injured & AttackCount in {country}'),
        dcc.Graph(figure=fig)
    ]
