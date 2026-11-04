# Task 3: Exploratory Data Analysis (EDA)

## Objective
Explore retail sales data to find patterns, trends, and relationships before building models.

## Files
- `task3_eda.py`: EDA script
- `Task3_Report.docx`: report to complete and submit
- Input: `../retail_sales_raw.csv`

## Analysis Performed
- Dataset shape and descriptive statistics
- Sales totals, counts, and averages by category and region
- Sales trend over time (monthly)
- Correlations among `units_sold`, `unit_price`, `sales_amount`, and `customer_rating`

## How to Run
```bash
pip install pandas matplotlib seaborn
cd Task3_EDA
python task3_eda.py
```

## Outputs
- `eda_category_sales.png`: sales by product category
- `eda_sales_trend.png`: sales over time
- `eda_correlation_heatmap.png`: correlation heatmap
- Console output: summary statistics, sales by category and region, and the correlation table

## Submission
Use the printed summaries and charts to describe the strongest category and region, add the outputs to `Task3_Report.docx`, fill in the student name, and upload the files listed in the task's Submit Work page on the Thiranex website.
