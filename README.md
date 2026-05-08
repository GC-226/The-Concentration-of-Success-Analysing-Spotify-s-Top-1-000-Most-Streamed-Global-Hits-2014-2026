# The Concentration of Success: Analysing Spotify’s Top 1,000 Most Streamed Global Hits (2014–2026)

## Project Overview
This project explores whether people turn to more upbeat, danceable, or escapist music during economic uncertainty using Spotify global chart data. 

It demonstrates web scraping, data cleaning, visualisation, and regression analysis.

---

## How to Replicate This Project

### Install Required Packages
```bash
python -m pip install -r requirements.txt
```

### Run the Analysis Scripts
```bash
python scripts/01_scrape_charts.py
python scripts/02_clean_data.py
python scripts/03_analysis.py
```

### View the Blog Post
Open blog.ipynb and run all

## Packages & Versions Used

| Package              | Version     | Purpose |
|----------------------|-------------|---------|
| pandas               | 3.0.2       | Data manipulation & cleaning |
| numpy                | 2.4.4       | Numerical computations |
| matplotlib           | 3.10.9      | Plotting |
| seaborn              | 0.13.2      | Statistical visualizations |
| plotly               | 6.7.0       | Interactive plots |
| statsmodels          | 0.14.6      | Regression analysis (Unit 5) |
| scikit-learn         | 1.6.1       | Machine learning tools |
| requests             | 2.33.1      | Web requests |
| beautifulsoup4       | 4.14.3      | Web scraping |
| lxml                 | 5.3.1       | HTML parsing |
| jupyter              | 1.0.0       | Notebook environment |

### Tools & Techniques Used
Web Scraping: requests + BeautifulSoup
Data Processing: pandas
Visualisation: matplotlib + seaborn
Statistical Modelling: statsmodels (OLS Regression)
Version Control: Git + GitHub

