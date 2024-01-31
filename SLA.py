import pandas as pd

file_path = 'jira-search.xlsx'
sheet_name = 'Your Jira Issues'
data = pd.read_excel(file_path, sheet_name=sheet_name)

def check_time(time):
    if time < 0:
        return 'Breached'
    else:
        return 'Met'

data['SLA TTFR'] = data['Time to first response (Elapsed Minutes)'].apply(check_time)
data['SLA TTR'] = data['Time to resolution (Elapsed Minutes)'].apply(check_time)

data.to_excel(file_path, sheet_name=sheet_name, index=False)