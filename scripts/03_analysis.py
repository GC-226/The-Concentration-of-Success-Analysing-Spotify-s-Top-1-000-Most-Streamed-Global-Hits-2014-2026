import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np

print("Starting analysis...")

df = pd.read_csv("data/processed/spotify_cleaned.csv")

# Create output folder
Path("output/plots").mkdir(parents=True, exist_ok=True)

# Plot 1: Top 10 Artists
plt.figure(figsize=(12, 6))
top_artists = df.groupby('artist')['total_streams_while_in_Top_200 (millions)'].sum().sort_values(ascending=False).head(10)
top_artists.plot(kind='bar', color='skyblue')
plt.title('Top 10 Artists by Total Streams')
plt.ylabel('Total Streams (Billions)')
plt.xlabel('Artist')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('output/plots/top_10_artists.png', dpi=300)
plt.close()

# Plot 2: Streams Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['total_streams_while_in_Top_200 (millions)'], bins=50, kde=True, color='blue')
plt.title('Distribution of Total Streams Across Top 1,000 Songs (Log Scale)')
plt.xlabel('Total Streams')
plt.xscale('log')
plt.ylabel('Number of Songs')
plt.tight_layout()
plt.savefig('output/plots/streams_distribution.png', dpi=300)
plt.close()

# Plot 3: Top 10 Songs
plt.figure(figsize=(12, 6))
top_songs = df.nlargest(10, 'total_streams_while_in_Top_200 (millions)')
sns.barplot(data=top_songs, y='title', x='total_streams_while_in_Top_200 (millions)', hue='artist', dodge=False)
plt.title('Top 10 Individual Songs by Total Streams')
plt.xlabel('Total Streams')
plt.ylabel('')
plt.tight_layout()
plt.savefig('output/plots/top_10_songs.png', dpi=300)
plt.close()

print("Analysis finished")