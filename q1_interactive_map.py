"""
Q1: Interactive Geographic Map of Economic Connectedness

This script creates an interactive choropleth map showing Economic Connectedness
by US county using Plotly.
"""

import pandas as pd
import plotly.graph_objects as go
from urllib.request import urlopen
import json

# Load county data
print("Loading county data...")
df = pd.read_csv('data/social_capital_county.csv')

# Convert county codes to 5-digit FIPS codes (zero-padded)
df['fips'] = df['county'].astype(str).str.zfill(5)

# Parse county name and state
df[['county_only', 'state']] = df['county_name'].str.split(', ', expand=True)

print(f"Loaded {len(df)} counties")
print(f"Counties with EC data: {df['ec_county'].notna().sum()}")
print(f"Counties without EC data: {df['ec_county'].isna().sum()}")

# Load GeoJSON for US counties
print("\nLoading US counties GeoJSON...")
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Create hover text
df['hover_text'] = df.apply(
    lambda row: f"{row['county_only']}, {row['state']}<br>" +
                f"County Code: {row['fips']}<br>" +
                f"Economic Connectedness: {row['ec_county']:.3f}" if pd.notna(row['ec_county'])
                else f"{row['county_only']}, {row['state']}<br>" +
                     f"County Code: {row['fips']}<br>" +
                     f"Economic Connectedness: NA",
    axis=1
)

# Create the choropleth map
print("\nCreating interactive map...")
fig = go.Figure(go.Choroplethmapbox(
    geojson=counties,
    locations=df['fips'],
    z=df['ec_county'],
    colorscale='RdYlBu',  # Red-Yellow-Blue colorscale
    zmid=df['ec_county'].median(),  # Center colorscale at median
    text=df['hover_text'],
    hovertemplate='%{text}<extra></extra>',
    marker_opacity=0.7,
    marker_line_width=0.5,
    marker_line_color='white',
    colorbar=dict(
        title="Economic<br>Connectedness",
        thickness=15,
        len=0.7,
        x=0.95
    )
))

# Update layout
fig.update_layout(
    title={
        'text': 'Economic Connectedness by US County',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 20, 'family': 'Arial'}
    },
    mapbox_style="carto-positron",
    mapbox_zoom=3,
    mapbox_center={"lat": 37.0902, "lon": -95.7129},  # Center of US
    height=700,
    margin={"r":0,"t":50,"l":0,"b":0}
)

# Save the interactive map
output_file = 'q1_economic_connectedness_map.html'
fig.write_html(output_file)
print(f"\nInteractive map saved to: {output_file}")

# Also display in notebook (if running in Jupyter)
try:
    fig.show()
except:
    print("Map created successfully! Open the HTML file to view it.")
