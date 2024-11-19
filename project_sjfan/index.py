from dash import html
import dash_bootstrap_components as dbc
from app import app

from header import HeaderInfo
from filteritem import FilterInfo
from stackbarline import StackBarLineInfo
from piechart import PieInfo
from mapchart import MapInfo

app.layout = html.Div(
    [
        html.Div([HeaderInfo()], style={'height': '10%', 'margin-top': '0px', 'padding-top': '0px'}),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col([FilterInfo()], className='card_container'),
                        dbc.Col([StackBarLineInfo()], className='card_container'),
                        dbc.Col([PieInfo()], className='card_container')
                    ],
                    style={'height': '45%', 'margin-top': '0px', 'padding-top': '0px'}
                )
            ],
            style={'height': '45%', 'margin-top': '0px', 'padding-top': '0px'}
        ),
        html.Div([MapInfo()], className='card_container', style={'height': '45%', 'margin-left': '0px', 'margin-right': '5px', 'margin-top': '0px', 'padding-top': '0px'})
    ],
    style={ 'margin': '0', 'padding': '0'}
)

if __name__ == '__main__':
    app.run_server(debug=True)
