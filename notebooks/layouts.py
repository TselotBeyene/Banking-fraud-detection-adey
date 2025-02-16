from dash import html, dcc
import dash_bootstrap_components as dbc

# Helper function to generate KPI Cards
def create_kpi_card(title, id, color):
    return dbc.Col(
        dbc.Card([
            dbc.CardBody([
                html.H4(title, className="card-title"),
                html.P("Loading...", id=id, className="card-text")
            ])
        ], color=color, inverse=True),
        width=4,
        className="p-2"
    )

# Function to create the layout
def create_layout():
    return dbc.Container(
        [
            # Navigation Bar with Enhanced Design
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(dbc.NavLink("Home", href="/", style={"color": "#FFFFFF"})),
                ],
                brand="Fraud Detection Dashboard",
                brand_style={"color": "#FFFFFF", "fontSize": "1.5rem", "fontWeight": "bold"},
                brand_href="/",
                color="rgb(61, 105, 153)",
                dark=True,
                style={"fontFamily": "Montserrat, sans-serif", "fontWeight": "bold"},
                className="mb-4",  # Margin below the navbar
            ),

            # KPI Cards Row
            dbc.Row([
                create_kpi_card("Total Transactions", "total-transactions", "primary"),
                create_kpi_card("Fraud Cases", "fraud-cases", "danger"),
                create_kpi_card("Fraud Percentage", "fraud-percentage", "info")
            ], justify="center", className="mb-4"),

            # Graph Row
            dbc.Row([
                dbc.Col([dcc.Graph(id="fraud-over-time")], width=12)
            ], className="p-4 mb-4", style={"background-color": "#f8f9fa"}),  # Light background for the chart

            # Browser and Sex Charts Row
            dbc.Row([
                dbc.Col([dcc.Graph(id="fraud-by-browser")], width=6, className="p-2"),
                dbc.Col([dcc.Graph(id="fraud-by-sex")], width=6, className="p-2")
            ], className="p-4 mb-4", style={"background-color": "#f8f9fa"}),

            # Fraud by Country Map Row
            dbc.Row([
                dbc.Col([dcc.Graph(id="fraud_by_country_map")], width=12, className="p-2")  # Full width for the country map
            ], className="p-4 mb-4", style={"background-color": "#f8f9fa"}),

            # Fraud Class Chart Row
            dbc.Row([
                dbc.Col([dcc.Graph(id="fraud-class")], width=6, className="p-2", style={"background-color": "#f8f9fa"}),
                dbc.Col([dcc.Graph(id="fraud-by-age-bin")], width=6, className="p-2", style={"background-color": "#f8f9fa"})
            ], className="p-4 mb-4"),
        ],

        fluid=True,
        style={
            "background-color": "#e9ecef", 
            "padding": "10px",
            "max-width": "90%",  # Recommended width for readability and spacing
            "margin": "auto"  # Centers the container within the page
        }
    )
