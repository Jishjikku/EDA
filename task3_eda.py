# Task 3: Exploratory Data Analysis (EDA)
# Run: python task3_eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "retail_sales_raw.csv"
OUT = Path(__file__).resolve().parent
df = pd.read_csv(DATA)
df = df.drop_duplicates()
df["customer_rating"] = df["customer_rating"].fillna(df["customer_rating"].median())
df["region"] = df["region"].fillna("Unknown")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date","sales_amount"])

print("Dataset shape:", df.shape)
print("\nNumerical summary:\n", df.describe(numeric_only=True))
print("\nSales by category:\n", df.groupby("category")["sales_amount"].agg(["count","mean","sum"]).sort_values("sum", ascending=False))
print("\nSales by region:\n", df.groupby("region")["sales_amount"].sum().sort_values(ascending=False))
print("\nCorrelation:\n", df[["units_sold","unit_price","sales_amount","customer_rating"]].corr(numeric_only=True))

df.groupby("category")["sales_amount"].sum().sort_values(ascending=False).plot(kind="bar", title="Sales by Product Category")
plt.ylabel("Total sales"); plt.tight_layout(); plt.savefig(OUT/"eda_category_sales.png", dpi=150); plt.close()
df.groupby(df["date"].dt.to_period("M"))["sales_amount"].sum().plot(marker="o", title="Sales Over Time")
plt.ylabel("Total sales"); plt.tight_layout(); plt.savefig(OUT/"eda_sales_trend.png", dpi=150); plt.close()
sns.heatmap(df[["units_sold","unit_price","sales_amount","customer_rating"]].corr(numeric_only=True), annot=True, cmap="Blues")
plt.title("Correlation Heatmap"); plt.tight_layout(); plt.savefig(OUT/"eda_correlation_heatmap.png", dpi=150); plt.close()
print("Charts saved to:", OUT)
