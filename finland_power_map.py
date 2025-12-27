import pandas as pd
import plotly.graph_objects as go

# Load data from CSV (recommended for GitHub)
# df = pd.read_csv("finland_power_data.csv")

# For demo purpose, data is inline
data = {
    "Region": ["Uusimaa", "Southeast Finland", "Pirkanmaa", "Southwest Finland",
               "North Savo", "South Ostrobothnia", "Central Finland",
               "North Ostrobothnia", "Lapland"],
    "Baseline": [16704, 4847, 5804, 4847, 3349, 2092, 4365, 5456, 6223],
    "Demand_100": [21608, 6001, 7118, 5958, 4133, 2592, 5306, 6606, 7516],
    "Production": [10247, 796, 1154, 796, 1031, 1962, 2934, 9943, 7173],
    "Latitude": [60.2, 60.9, 61.5, 60.5, 63.0, 62.8, 62.2, 65.0, 67.5],
    "Longitude": [24.9, 27.7, 23.8, 22.3, 27.7, 23.0, 25.7, 25.5, 26.5]
}

df = pd.DataFrame(data)

# Function to plot scenarios
def plot_all_scenarios(df):
    baseline_trace = go.Scattermapbox(
        lat=df["Latitude"],
        lon=df["Longitude"] - 0.4,
        mode='markers',
        marker=go.scattermapbox.Marker(size=df["Baseline"] / 220, color="green"),
        name="Consumption (Baseline)"
    )

    demand100_trace = go.Scattermapbox(
        lat=df["Latitude"],
        lon=df["Longitude"],
        mode='markers',
        marker=go.scattermapbox.Marker(size=df["Demand_100"] / 220, color="orange"),
        name="Consumption (50% EV Demand)"
    )

    production_trace = go.Scattermapbox(
        lat=df["Latitude"],
        lon=df["Longitude"] + 0.4,
        mode='markers',
        marker=go.scattermapbox.Marker(size=df["Production"] / 220, color="blue"),
        name="Production"
    )

    label_traces = []
    for i, row in df.iterrows():
        text_pos = "top center"
        label_lat = row["Latitude"] + 0.2
        label_lon = row["Longitude"]
        if row["Region"] == "Southwest Finland":
            text_pos = "middle left"
            label_lon -= 0.7
        elif row["Region"] == "Uusimaa":
            text_pos = "middle right"
            label_lon += 1.8

        trace = go.Scattermapbox(
            lat=[label_lat],
            lon=[label_lon],
            mode='markers+text',
            marker=go.scattermapbox.Marker(size=1, color='rgba(0,0,0,0)'),
            text=[row["Region"]],
            textposition=text_pos,
            showlegend=False
        )
        label_traces.append(trace)

    fig = go.Figure(data=[baseline_trace, demand100_trace, production_trace] + label_traces)

    fig.update_layout(
        mapbox=dict(center=dict(lat=63.8, lon=26), zoom=3.9, style="carto-positron"),
        margin={"r": 0, "t": 50, "l": 0, "b": 0},
        title="Electricity Production and Consumption in Finland (Baseline vs 50% EV Demand)"
    )
    return fig

# Run the plot
fig = plot_all_scenarios(df)
fig.show()
