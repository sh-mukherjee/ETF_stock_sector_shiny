import plotly.express as px
from shiny import App, ui, reactive
from shinywidgets import render_plotly

from ETF_sector_data_prep import sector_df, countries

# Define the app UI
app_ui = ui.page_fluid(
    ui.h1("MSCI ETF Sector Weights"),
    ui.p("Source: Yahoo! Finance"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_selectize(
                'Country', 'Select Country', countries, multiple=True
            )
        ),
        ui.panel_main(
            ui.output_plot('sector_plot')
        )
    )
)

# Server logic
def server(input, output, session):
    @reactive.Calc
    def filter_data():
        mask = sector_df.Country.isin(input.Country())
        return sector_df[mask]

    @output
    @render_plotly
    def sector_plot():
        data = filter_data()
        return px.bar(
            data,
            x="Weight(%)",
            y="Sector_Name",
            color="Country",
            hover_data=['Country', 'Sector_Name', 'Weight(%)'],
            color_discrete_map={
                "Japan": "red",
                "Taiwan": "#00CC96",
                "South Korea": "blue",
                "Hong Kong": "#FBE426",
                "Singapore": "magenta",
                "Australia": "brown",
                "Malaysia": "green",
                "Thailand": "darkblue"
            },
            template="ggplot2",
            barmode='group',
            height=800
        )

# Run the app
app = App(app_ui, server)
