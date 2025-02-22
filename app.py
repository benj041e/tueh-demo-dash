# ***************************************
# Imports
# ***************************************
# Dash
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Div.
import pandas as pd
import numpy as np
import calendar

# Plotly
import plotly.express as px
import plotly.graph_objects as go

# ***************************************
# Get data
# ***************************************
import datamodel
order = datamodel.get_data()
df_year = datamodel.get_year()
df_month = datamodel.get_month()

# ***************************************
# Diagram - Employee Sales
# ***************************************
fig_employee = px.bar(order, 
    x='emp_name', y='total', 
    color='type', text='total', title='Sales by Employee',
    hover_data=[],
    labels={'total':'Total sales', 'emp_name':'Employee', 'type':'Product Type'})
fig_employee.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_employee.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

ord_employee = px.bar(order, 
    x='productname', y='total', 
    color='type', text='total', title='Sales by Product',
    hover_data=[],
    labels={'total':'Total sales', 'productname':'Products', 'type':'Product Type'})
ord_employee.update_traces(texttemplate='%{text:.2s}', textposition='outside')
ord_employee.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)


# ***************************************
# Activate the app
# ***************************************
#app = dash.Dash(__name__)

dash_app = dash.Dash(__name__)
app = dash_app.server

# ***************************************
# Layout
# ***************************************
dash_app.layout = html.Div(
    children=[
        html.Div(className='row',
                children=[
                    html.Div(className='eight columns div-for-charts bg-grey',
                            children=[
                                dcc.Graph(id="sales_employee", figure=fig_employee),
                                dcc.Graph(id="sales_product", figure=ord_employee)
                            ]
                    ),
                ]
            )
        ]
)

# ***************************************
# Run the app
# ***************************************
if __name__ == '__main__':
    dash_app.run_server(debug=True)
