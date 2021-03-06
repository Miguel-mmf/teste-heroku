import dash_core_components as dcc
import dash_html_components as html

import dash_table
from dash_table.Format import Format, Scheme, Sign, Symbol

from app import app
from apps import app_dashboard_v01

def init_user_data():
    return {
    }

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def gera_layout():

    return html.Div(
        [
            html.H2(
                ['Visualização em Tabela'],
                className='title_style',
            ),

            html.Hr(className='hr'),

            html.H6(
                [
                    'Essa é a planilha de dados obtida a partir da organização das informações do arquivo {}'
                .format(app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['filename'])
                ],
                className='subtitle_style',
            ),

            gera_tabela()
        ],
        style={'margin-left':'20px','margin-right':'20px'}
    )

def gera_tabela():

    df = app.dict_apps['app_dashboard_v01']['series_df']

    return html.Div(
        [
            dash_table.DataTable(

                data = df.to_dict('records'),

                columns = [
                    {
                        'name': col, 
                        'id': col,
                        'type': 'numeric',
                        'format': Format(precision=4, scheme=Scheme.fixed),
                    } 
                    for col in df.columns
                ],

                style_cell={
                    'textAlign': 'center',
                    'border': '1px solid grey',
                    'minWidth':'90px',
                    'width':'125px',
                    'maxWidth':'160px',
                    'fontSize':'14',
                    'color':'#c1ce13',
                    'font-family':'sans-serif',
                    'backgroundColor':'#061E44',
                    },
                    
                style_header={
                    'backgroundColor':'#c1ce13',
                    'color':'#061E44',
                    'fontWeight': 'bold'
                },

                page_size = 17,

                style_table = {
                    'height':'558px',
                    'minWidth': '100%',
                    'overflowX': 'auto'
                }
            )
        ],
        style={'margin-top':'15px'}
    )

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Fim das Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++ CALLBACKS  ++++++++++++++++