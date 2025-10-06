import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
DATA_PATH = Path("data/happiness_2021.csv")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(DATA_PATH)
print("Data loaded successfully!")
print(df.head())
print("Average Happiness Score:", df["HappinessScore"].mean())
if "LoggedGDPPerCapita" in df.columns:
    print("Correlation (GDP vs Happiness):", df["LoggedGDPPerCapita"].corr(df["HappinessScore"]))
    plt.figure(figsize=(10,5))
plt.bar(df["Country"], df["HappinessScore"], color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.title("Happiness Score by Country (2021)")
plt.ylabel("Happiness Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "happiness_plot.png")
plt.close()
print("Plot saved to output/happiness_plot.png")