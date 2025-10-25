# Applied-Machine-Learning-2025
Καλύπτουμε το πλήρες εύρος των σχετικών ικανοτήτων και τεχνογνωσίας, από την εύρεση και επεξεργασία δεδομένων, στην οπτικοποίηση και ερμηνεία τους, σε διαφορετικά μοντέλα και εφαρμογές Μηχανικής Μάθησης, μέχρι και Νευρωνικά Δίκτυα και αρχιτεκτονικές Βαθιάς Εκμάθησης. 

## Economic Connectedness Assignment

This repository contains an assignment on Economic Connectedness and Social Capital, replicating analyses from two Nature papers:
- Chetty et al. (2022) - Social capital I: measurement and associations with economic mobility
- Chetty et al. (2022) - Social capital II: determinants of economic connectedness

### Setup Instructions

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Launch Jupyter Notebook:
```bash
jupyter notebook economic_connectedness_assignment.ipynb
```

3. Run the cells in order. The notebook will automatically download data from the [Social Capital Atlas](https://data.humdata.org/dataset/social-capital-atlas).

### Assignment Structure

The notebook contains implementations for 5 questions:
- **Q1**: Interactive map of Economic Connectedness by county
- **Q2**: Scatter plot of upward income mobility vs economic connectedness
- **Q3**: Economic connectedness vs median household income (colored by upward mobility)
- **Q4**: Friending bias and exposure by high school
- **Q5**: Friending bias vs racial diversity (colleges and neighborhoods)

### Data Sources

All data is downloaded automatically from:
- [Social Capital Atlas Datasets](https://data.humdata.org/dataset/social-capital-atlas)
- County-level, ZIP code-level, high school-level, and college-level data

### Requirements

- Python 3.7+
- Internet connection for downloading data
- Libraries: pandas, numpy, matplotlib, seaborn, scipy, plotly, jupyter
