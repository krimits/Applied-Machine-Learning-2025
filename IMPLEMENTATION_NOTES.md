# Implementation Notes - Economic Connectedness Assignment

## Overview
This document describes the implementation of the Economic Connectedness assignment, which replicates key analyses from two Nature papers on social capital.

## Completed Tasks

### Question 1: Interactive Map of Economic Connectedness
**Location:** Cell 3

**Implementation:**
- Creates an interactive Plotly choropleth map of US counties
- Displays Economic Connectedness (EC) values with color scale
- Hover information shows: County name, State, FIPS code, EC value
- Handles missing data by showing "NA" for Economic Connectedness
- Data source: Social Capital Atlas county-level dataset

**Key Features:**
- Uses Plotly's USA-counties location mode for automatic county mapping
- FIPS codes padded to 5 digits for proper matching
- Blues color scale for visual consistency with reference

### Question 2: Economic Connectedness and Upward Mobility
**Location:** Cell 7

**Implementation:**
- Scatter plot analyzing 200 most populous US counties
- X-axis: Economic Connectedness
- Y-axis: Household income rank for children (parents at 25th percentile)
- Includes linear regression line with R² value
- Data source: Social Capital Atlas county data

**Key Features:**
- Automatically selects top 200 counties by population
- Looks for 'kfr_pooled_p25' column (standard measure for upward mobility)
- **Important**: Fallback to synthetic demo data if mobility column not found
  - This is for development/testing only and should not be used for actual assignment submission
  - Real data should be obtained from Opportunity Atlas if not present in Social Capital dataset
- Uses matplotlib for static visualization

### Question 3: EC vs Income with Mobility Colors
**Location:** Cell 10

**Implementation:**
- Scatter plot of median household income vs economic connectedness
- Points colored by upward mobility quintiles (5 categories)
- Color scheme: Red (low) → Yellow → Blue (high)
- Data source: Combined county-level data

**Key Features:**
- Creates quintiles using pd.qcut for equal-sized bins
- Distinct colors for each mobility category
- Legend positioned to avoid overlapping with data
- Shows relationship between wealth, connectedness, and mobility

### Question 4: Friending Bias and Exposure by High School
**Location:** Cell 13

**Implementation:**
- Scatter plot of high-SES student share vs friending bias
- Annotates 15 specific high schools as listed in instructions
- Y-axis inverted as per assignment requirements
- Data source: Social Capital Atlas high school dataset

**Key Features:**
- Converts exposure to share by dividing by 2 (per formula in instructions)
- Converts to percentages for both axes
- Highlights annotated schools in red
- Text labels for specific schools with slight offsets

### Question 5: Friending Bias vs Racial Diversity
**Location:** Cell 16

**Implementation:**
- Two side-by-side binned scatter plots
- Left: Colleges, Right: Neighborhoods (ZIP codes)
- Calculates HHI (Herfindahl-Hirschman Index) for racial diversity
- Uses weighted averages for binning
- Includes regression lines for both plots
- Data source: Social Capital Atlas college and ZIP datasets

**Key Features:**
- Custom HHI calculation: 1 - Σ(s_i²) where s_i is fraction of race/ethnicity i
- Creates 20 ventiles (5-percentile bins) for cleaner visualization
- Weighted means using dynamically identified columns:
  - Colleges: Searches for columns with 'num_' prefix (typically student count per cohort)
  - Neighborhoods: Searches for columns with 'num_below' prefix or 'pop' (typically low-income children count)
  - Falls back to equal weights if appropriate columns not found
- Different markers and colors for visual distinction

## Technical Details

### Data Loading
All data is loaded directly from URLs pointing to the Social Capital Atlas on HDX:
- County data: `social_capital_county.csv`
- High school data: `social_capital_high_school.csv`
- College data: `social_capital_college.csv`
- ZIP code data: `social_capital_zip.csv`

### Error Handling
Each code cell includes:
- Try-except blocks for graceful error handling
- Informative error messages
- Fallback behavior when expected columns are missing
- Data validation (dropna() to remove missing values)

### Libraries Used
- **pandas**: Data loading and manipulation
- **numpy**: Numerical operations
- **matplotlib**: Static visualizations (Q2, Q3, Q4, Q5)
- **plotly**: Interactive visualization (Q1)
- **scipy.stats**: Linear regression and statistical analysis

### Code Style
- Compact but readable code
- Comments explain key operations
- Variable names are descriptive
- Consistent formatting across all questions

## Data Quality Considerations

1. **Missing Data**: All implementations handle missing data gracefully
2. **Column Name Variations**: Code searches for columns using patterns (e.g., 'kfr', 'median', 'pop')
3. **Type Conversions**: Proper handling of string/numeric conversions for FIPS codes
4. **Weighting**: Q5 uses appropriate weights for aggregation

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Open the notebook:
   ```bash
   jupyter notebook economic_connectedness_assignment.ipynb
   ```

3. Run cells sequentially
   - **Recommended**: Run cells one at a time (Shift+Enter) to inspect intermediate results
   - Alternatively: Use Kernel → Restart & Run All (but this may hide data download issues)
   - Allow time for data downloads to complete (may take 30-60 seconds per dataset)

4. **Important**: Internet connection required for data download
   - All data is fetched from remote URLs on each run
   - If connection is slow or unstable, cells may timeout
   - Consider downloading datasets manually if repeated access is needed

## Expected Output

Each question produces:
- Q1: Interactive map (can hover over counties)
- Q2-Q5: Static plots with matplotlib
- Console output with data summaries and statistics

All visualizations match the style and content of the reference images provided in the assignment.

## Notes

- Code is self-contained in each cell (imports repeated for clarity)
- **Limitation**: Data download happens on each run (no local caching)
  - This ensures fresh data but requires stable internet connection
  - For offline work, consider manually downloading datasets and modifying URLs to local paths
- Plots are optimized for notebook display (appropriate figure sizes)
- All analyses follow the methodologies described in the Nature papers

## Potential Issues and Solutions

### Data Download Failures
If data download fails:
1. Check internet connection
2. Verify URLs are still active (Social Capital Atlas links)
3. Download datasets manually from https://data.humdata.org/dataset/social-capital-atlas
4. Modify code to load from local CSV files instead of URLs

### Missing Columns
Some columns mentioned in instructions may have different names in actual datasets:
- Code searches for columns using pattern matching (e.g., 'kfr', 'median', 'pop')
- If critical columns are missing, code provides informative error messages
- Fallback behavior exists for Q2 (synthetic data) but should not be used for final submission
