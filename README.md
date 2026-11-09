# Sales Data Analysis Project

## Project overview
This project analyzes a sales dataset using Python. It demonstrates data cleaning, exploratory data analysis (EDA), business metrics, visualizations, and actionable recommendations.

**Important:** `data/sales_data.csv` is an illustrative, synthetic dataset created for this project. It is not real company/customer data. Replace it with your internship-provided dataset before claiming findings about an actual business.

## Tools and technologies
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook (optional; analysis is also provided as a Python script)

## Project structure
```text
Sales_Data_Analysis_Project/
├── data/
│   └── sales_data.csv
├── src/
│   └── analysis.py
├── outputs/
│   ├── monthly_sales_trend.png
│   ├── sales_by_region.png
│   ├── sales_by_category.png
│   ├── sales_dashboard_screenshot.png
│   └── cleaned_sales_data.csv
├── Project_Report.pdf
├── requirements.txt
└── README.md
```

## How to run
1. Install Python 3.10 or later.
2. Open a terminal in this project folder.
3. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python src/analysis.py
   ```

## Analysis workflow
1. Load the CSV dataset.
2. Inspect rows, columns, data types, and missing values.
3. Remove duplicate records and handle missing values.
4. Calculate sales as `Quantity × Unit_Price × (1 − Discount)`.
5. Analyze sales by month, region, category, product, and customer type.
6. Generate charts and export cleaned data.

## Key metrics from the included sample
- Total sales: ₹13,999,724.74
- Unique orders: 600
- Average sales per order: ₹23,332.87
- Highest-sales region: West
- Highest-sales category: Electronics
- Highest-sales product: Office Chair

## Business recommendations
- Review inventory and marketing investment in the strongest sales region and category.
- Investigate low-performing categories and months before changing budgets.
- Encourage repeat purchases through customer retention offers.
- Track monthly sales regularly to identify seasonal patterns.

## GitHub submission
Create a new public GitHub repository named `sales-data-analysis`, upload all files from this folder, and copy the repository URL into the internship submission form. Do not submit the example URL; use your actual repository URL.
