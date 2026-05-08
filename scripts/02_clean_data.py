import pandas as pd
from pathlib import Path

print("Starting data cleaning")

# Load raw data
df = pd.read_csv("data/raw/spotify_global_weekly_totals.csv")

print("Column names in raw file:", df.columns.tolist())

# Make copy
df_clean = df.copy()

# Rename first column to 'track_name'
df_clean = df_clean.rename(columns={df_clean.columns[0]: 'track_name'})

# Split Artist and Title
df_clean[['artist', 'title']] = df_clean['track_name'].str.split(' - ', n=1, expand=True)

# Rename streams column
streams_col = df_clean.columns[1]
df_clean = df_clean.rename(columns={streams_col: 'total_streams_while_in_Top_200 (millions)'})

# Clean streams number
df_clean['total_streams_while_in_Top_200 (millions)'] = pd.to_numeric(
    df_clean['total_streams_while_in_Top_200 (millions)'].astype(str).str.replace(',', '').str.replace('.', ''), 
    errors='coerce'
)

# Drop missing values
df_clean = df_clean.dropna(subset=['artist', 'title', 'total_streams_while_in_Top_200 (millions)'])

# Keep top 1000 most streamed tracks
df_clean = df_clean.sort_values('total_streams_while_in_Top_200 (millions)', ascending=False).head(1000).reset_index(drop=True)

# Save cleaned data
Path("data/processed").mkdir(parents=True, exist_ok=True)
df_clean.to_csv("data/processed/spotify_cleaned.csv", index=False)

print(f"Cleaned data saved successfully. Shape: {df_clean.shape}")
print("\nTop 10 tracks:")
print(df_clean[['artist', 'title', 'total_streams_while_in_Top_200 (millions)']].head(10))

print("\nCleaning completed")