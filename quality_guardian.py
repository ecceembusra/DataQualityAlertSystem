import logging
import smtplib
from email.mime.text import MIMEText
import pandas as pd

# Logger settings
logging.basicConfig(filename='data_quality_alerts.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def send_email_alert(subject, body, to_email):
    from_email = 'example@gmail.com' # replace with your email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, 'password')  # replace with your actual app password
            server.send_message(msg)
        print(f"Email successfully sent to: {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def data_quality_check(df):
    alerts = []

    # Null value check
    null_cols = ['order_id', 'customer_id', 'order_date']
    for col in null_cols:
        null_count = df[col].isnull().sum()
        if null_count > 0:
            msg = f"Null values found: {null_count} nulls in column '{col}'."
            alerts.append(msg)
            logging.warning(msg)

    # Duplicate ID check
    if df['order_id'].duplicated().any():
        dup_count = df['order_id'].duplicated().sum()
        msg = f"Duplicate order_id values found: {dup_count} duplicates."
        alerts.append(msg)
        logging.warning(msg)

    # Outlier check for high order_amount
    if (df['order_amount'] > 10000).any():
        outlier_count = (df['order_amount'] > 10000).sum()
        msg = f"Outlier order amounts detected: {outlier_count} orders exceeding 10,000."
        alerts.append(msg)
        logging.warning(msg)
    # Alert report
    if alerts:
        alert_report = "\n".join(alerts)
        print("📢 Data Quality Alert:\n", alert_report)
        send_email_alert("Data Quality Alert", alert_report, "example@gmail.com") # replace with your mail
    else:
        print("✅ Data quality checks passed. No issues found.")

# Example usage
if __name__ == "__main__":
    try:
        df = pd.read_csv('orders.csv')
        data_quality_check(df)
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        print(f"An error occurred: {e}")

