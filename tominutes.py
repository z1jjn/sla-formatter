import pandas as pd

file_path = 'jira-search.xlsx'
sheet_name = 'Your Jira Issues'

data = pd.read_excel(file_path, sheet_name=sheet_name)

def convert_time_format(time_str):
    if len(str(time_str)) > 0:
        split = str(time_str).split(' ')
        if len(split) == 1:
            if str(split[0][-1]).endswith('h'):
                final_value = int(split[0][:-1].replace(",", ""))
                return f"{final_value*60}"
            if str(split[0][-1]).endswith('m'):
                final_value = int(split[0][:-1].replace(",", ""))
                return f"{final_value}"
        elif len(split) == 2:
            hour = str(split[0][:-1].replace(",", ""))
            minute = str(split[1][:-1].replace(",", ""))
            if hour[0] == "-":
                hours = abs(int(hour))
                minutes = int(minute)
                return f"-{(hours*60)+minutes}"
            else:
                hours = int(hour)    
                minutes = int(minute)
                return f"{(hours*60)+minutes}"
        
data['Time to first response (Elapsed Minutes)'] = data['Time to first response (Elapsed Minutes)'].apply(convert_time_format)
data['Time to resolution (Elapsed Minutes)'] = data['Time to resolution (Elapsed Minutes)'].apply(convert_time_format)

data.to_excel(file_path, sheet_name=sheet_name, index=False)