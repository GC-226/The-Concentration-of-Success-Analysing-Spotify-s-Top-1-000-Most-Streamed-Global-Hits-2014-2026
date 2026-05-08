import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

# Create folders if they don't exist
Path("data/raw").mkdir(parents=True, exist_ok=True)

print("Starting to scrape Spotify Charts from Kworb.net")

def scrape_kworb(url, filename):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        
        if table is None:
            print(f"No table found on {url}")
            return None
            
        df = pd.read_html(str(table))[0]
        df.to_csv(f"data/raw/{filename}", index=False)
        print(f"Successfully saved {len(df)} rows to data/raw/{filename}")
        return df
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Scrape Current Global Weekly Chart
scrape_kworb(
    "https://kworb.net/spotify/country/global_weekly.html", 
    "spotify_global_weekly_current.csv"
)

# Scrape Historical Totals
scrape_kworb(
    "https://kworb.net/spotify/country/global_weekly_totals.html", 
    "spotify_global_weekly_totals.csv"
)

print("\nScraping completed. Check 'data/raw' folder.")