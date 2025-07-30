# DataQualityAlertSystem
A lightweight Python-based tool for validating datasets and triggering alerts when data quality issues are detected. This project is perfect for analysts, data engineers, and anyone responsible for maintaining clean, reliable data pipelines.

## 🚀 Features

- 📛 Null value detection  
- 🔁 Duplicate ID detection  
- 💸 Outlier detection (e.g., order amounts > 10,000)  
- 📬 Automated email alerts via Gmail SMTP  
- 🪵 Logging to local .log file for traceability

## 🛠 How It Works

The script checks for common data quality issues in your dataset (like missing fields, duplicate records, or suspiciously large values). When an issue is found, it logs it and can also send you a notification email directly via Gmail.

## 📂 Sample Input

```csv
order_id,customer_id,order_date,order_amount
1001,C001,2025-07-01,250
1002,C002,2025-07-02,800
1003,C003,,450
1004,,2025-07-04,11000
1005,C005,2025-07-05,130
1005,C006,2025-07-06,950
1006,C007,2025-07-07,12000
