# The Concentration of Success: Analysing Spotify’s Top 1,000 Most Streamed Global Hits (2014–2026)

## Project Overview

This project examines the concentration of success in the global music streaming industry by analysing the top 1,000 most streamed songs on Spotify’s Global chart from 2014 to 2026.

Using data scraped from Kworb.net, the study investigates how streaming success is distributed across artists and individual tracks. It explores key patterns such as artist dominance, the extreme skewness of stream distribution, and the relationship between chart performance (peak position and weeks in the Top 10) and total streams.

Through web scraping, data cleaning, visualisation, and regression analysis, this project highlights the “winner-takes-most” nature of modern digital music consumption.

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

### Project Structure
The-Concentration-of-Success-Analysing-Spotify-s-Top-1-000-Most-Streamed-Global-Hits-2014-2026/   
├── README.md  
├── requirements.txt  
├── blog.ipynb                  
├── data/  
│   ├── raw/  
│   └── processed/  
├── scripts/  
│   ├── 01_scrape_charts.py  
│   ├── 02_clean_data.py  
│   └── 03_analysis.py  
├── output/  
│   └── plots/  
├── .gitignore  
└── LICENSE  

### Packages & Versions Used

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

