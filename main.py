import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Define the layout for half-column graph
half_graph_layout = html.Div(
    className='half-column',
    children=[
        dcc.Graph(id='graph-1', figure={}),
    ]
)

# Define the layout for full-column graph
full_graph_layout = html.Div(
    className='full-column',
    children=[
        dcc.Graph(id='graph-2', figure={}),
    ]
)

# Define the layout for each row with graphs
row_graph_layout = html.Div(
    className='row',
    children=[
        half_graph_layout,
        half_graph_layout
    ]
)

# Define the layout for each row with DataTables
row_table_layout = html.Div(
    className='row',
    children=[
        dash_table.DataTable(
            id='datatable',
            columns=[
                {'name': 'Name', 'id': 'name'},
                {'name': 'Age', 'id': 'age'},
                {'name': 'City', 'id': 'city'}
            ],
            data=[
                {'name': 'John Doe', 'age': 30, 'city': 'New York'},
                {'name': 'Jane Smith', 'age': 25, 'city': 'London'},
                {'name': 'Bob Johnson', 'age': 35, 'city': 'Paris'}
            ]
        )
    ]
)

# Define the div containing the dropdowns
dropdown_div = html.Div(
    className='dropdowns',
    children=[
        dcc.Dropdown(
            id='period-dropdown',
            options=[
                {'label': 'Period 1', 'value': 'period-1'},
                {'label': 'Period 2', 'value': 'period-2'},
                {'label': 'Period 3', 'value': 'period-3'}
            ],
            value='period-1'
        ),
        dcc.Dropdown(
            id='level-dropdown',
            options=[
                {'label': 'Level 1', 'value': 'level-1'},
                {'label': 'Level 2', 'value': 'level-2'},
                {'label': 'Level 3', 'value': 'level-3'}
            ],
            value='level-1'
        )
    ]
)

# Define the overall dashboard layout
app.layout = html.Div(
    className='dashboard',
    children=[
        html.Div(
            className='upper-section',
            children=[
                dropdown_div
            ]
        ),
        row_graph_layout,
        full_graph_layout,
        row_table_layout,
        row_graph_layout
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
