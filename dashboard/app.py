import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("../data/data.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Dashboard Rendimiento Académico"),

    dcc.Dropdown(
        id="genero",
        options=[{"label": g, "value": g} for g in df["genero"].unique()],
        value="M"
    ),

    dcc.Graph(id="grafico"),

    dcc.Graph(
        figure=px.scatter(df, x="horas_estudio", y="nota_final", color="genero")
    )
])

@app.callback(
    Output("grafico", "figure"),
    Input("genero", "value")
)
def update_graph(genero):
    filtered = df[df["genero"] == genero]
    return px.histogram(filtered, x="nota_final")

if __name__ == "__main__":
    app.run(debug=True)