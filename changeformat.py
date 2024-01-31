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
                return f"{final_value:02d}:00"
            if str(split[0][-1]).endswith('m'):
                if str(split[0][0]) == "-":
                    final_value = int(split[0][1:-1].replace(",", ""))
                    return f"-0:{final_value:02d}"
                else:
                    final_value = int(split[0][:-1].replace(",", ""))
                    return f"0:{final_value:02d}"
        elif len(split) == 2:
            hour = str(split[0][:-1].replace(",", ""))
            minute = str(split[1][:-1].replace(",", ""))
            hours = int(hour)
            minutes = int(minute)
            return f"{hours:02d}:{minutes:02d}"
        
data['Time to first response'] = data['Time to first response'].apply(convert_time_format)
data['Time to resolution'] = data['Time to resolution'].apply(convert_time_format)

data.to_excel(file_path, sheet_name=sheet_name, index=False)