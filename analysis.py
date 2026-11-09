"""
Sales Data Analysis
Run: python src/analysis.py
Dataset: data/sales_data.csv (illustrative sample data)
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
print("Original rows:", len(df))
print("Missing values before cleaning:\n", df.isna().sum())
df = df.drop_duplicates()
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])
df["Discount"] = df["Discount"].fillna(0)
df = df.dropna(subset=["Order_Date", "Quantity", "Unit_Price"])
df["Sales"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("\\nCLEANED DATA SUMMARY")
print(df.describe(include="all"))
print("\\nTotal sales: ₹{:,.2f}".format(df["Sales"].sum()))
print("Unique orders:", df["Order_ID"].nunique())
print("Average sales per order: ₹{:,.2f}".format(df["Sales"].sum()/df["Order_ID"].nunique()))
print("\\nSales by region:\\n", df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
print("\\nSales by category:\\n", df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print("\\nTop products:\\n", df.groupby("Product")["Sales"].sum().nlargest(5))

monthly = df.groupby("Month")["Sales"].sum().sort_index()
plt.figure(figsize=(10,5))
sns.lineplot(x=monthly.index, y=monthly.values, marker="o")
plt.title("Monthly Sales Trend – 2025"); plt.xlabel("Month"); plt.ylabel("Sales (₹)")
plt.xticks(rotation=45); plt.tight_layout()
plt.savefig(OUT/"monthly_sales_trend.png", dpi=160); plt.close()

for column, filename, title in [
    ("Region", "sales_by_region.png", "Sales by Region"),
    ("Category", "sales_by_category.png", "Sales by Category")
]:
    values = df.groupby(column)["Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(9,5))
    sns.barplot(x=values.index, y=values.values)
    plt.title(title); plt.xlabel(column); plt.ylabel("Sales (₹)")
    plt.xticks(rotation=25, ha="right"); plt.tight_layout()
    plt.savefig(OUT/filename, dpi=160); plt.close()

df.to_csv(OUT/"cleaned_sales_data.csv", index=False)
print("\\nAnalysis complete. Charts and cleaned data saved in outputs/.")
