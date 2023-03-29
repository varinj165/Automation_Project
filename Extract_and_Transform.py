import pandas as pd
import csv

# Read data from the CRM system
crm_data = pd.read_csv('crm_data.csv')

# Read data from the customer feedback database
feedback_data = pd.read_csv('feedback_data.csv')

# Read data from the marketing campaign results spreadsheet
campaign_data = pd.read_excel('campaign_data.xlsx')

# Join the data from the three sources on a common customer ID
merged_data = pd.merge(crm_data, feedback_data, on='customer_id')
merged_data = pd.merge(merged_data, campaign_data, on='customer_id')

# Clean up the data and transform it into a standardized format
merged_data['date'] = pd.to_datetime(merged_data['date'], format='%Y-%m-%d')
merged_data['total_sales'] = merged_data['sales'] * merged_data['price']
merged_data['total_feedback'] = merged_data['feedback1'] + merged_data['feedback2'] + merged_data['feedback3']