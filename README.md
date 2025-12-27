# Finland Energy Visualization

## Problem
Visualize electricity production and consumption across different regions of Finland. Compare baseline consumption with projected EV demand and production.

## Solution
This project provides an interactive map using Python, pandas, and Plotly. Each region is plotted with scaled markers for baseline, 50% EV demand, and production.

## Data
- Baseline consumption
- 50% EV demand
- Production
- Latitude and Longitude of regions

## Usage
```python
import pandas as pd
import plotly.graph_objects as go
from finland_power_map import plot_all_scenarios

df = pd.read_csv("finland_power_data.csv")
fig = plot_all_scenarios(df)
fig.show()
