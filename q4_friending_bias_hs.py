"""
Q4: Friending Bias and Exposure by High School

This script creates a scatter plot showing the relationship between
the share of high-SES students and friending bias at the high school level.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load high school data
print("Loading high school data...")
df_hs = pd.read_csv('data/social_capital_high_school.csv')

# Calculate share of high-SES students (exposure / 2)
df_hs['share_high_ses'] = df_hs['exposure_parent_ses_hs'] / 2

# Convert to percentages
df_hs['share_high_ses_pct'] = df_hs['share_high_ses'] * 100
df_hs['bias_parent_ses_hs_pct'] = df_hs['bias_parent_ses_hs'] * 100

# Remove missing values
df_plot = df_hs.dropna(subset=['share_high_ses_pct', 'bias_parent_ses_hs_pct'])

print(f"Plotting {len(df_plot)} high schools")

# Annotated schools
annotated_schools = ['00941729', '060474000432', '170993000942', '170993001185', '170993003989',
                     '171449001804', '250327000436', '360009101928', '370297001285', '483702004138',
                     '250843001336', '062271003230', '010237000962', '00846981', '00852124']

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Scatter plot for all high schools
ax.scatter(df_plot['share_high_ses_pct'],
          df_plot['bias_parent_ses_hs_pct'],
          alpha=0.3,
          s=20,
          c='gray',
          label='High Schools')

# Highlight and annotate specific schools
df_annotated = df_plot[df_plot['high_school'].isin(annotated_schools)]

ax.scatter(df_annotated['share_high_ses_pct'],
          df_annotated['bias_parent_ses_hs_pct'],
          alpha=0.8,
          s=60,
          c='red',
          marker='o',
          edgecolors='darkred',
          linewidths=1.5,
          label='Annotated Schools',
          zorder=5)

# Add annotations for the specific schools
for idx, row in df_annotated.iterrows():
    # Use high school name for annotation if available, otherwise use code
    label = row['high_school_name'] if pd.notna(row['high_school_name']) else row['high_school']
    # Simplify label (just the school name without full address)
    if isinstance(label, str) and ',' in label:
        label = label.split(',')[0]

    ax.annotate(label,
               (row['share_high_ses_pct'], row['bias_parent_ses_hs_pct']),
               xytext=(5, 5),
               textcoords='offset points',
               fontsize=8,
               alpha=0.8,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

# Set labels and title
ax.set_xlabel('Share of High-SES Students (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Friending Bias (%)', fontsize=12, fontweight='bold')
ax.set_title('Friending Bias vs. Exposure by High School', fontsize=14, fontweight='bold', pad=20)

# Reverse y-axis as per assignment instructions
ax.invert_yaxis()

# Add grid
ax.grid(True, alpha=0.3, linestyle='--')

# Add legend
ax.legend(loc='best', framealpha=0.9)

# Tight layout
plt.tight_layout()

# Save figure
output_file = 'q4_friending_bias_exposure.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"\nFigure saved to: {output_file}")

plt.show()
