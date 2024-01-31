import pandas as pd

#change to your own slas, the number must be the minute
request_type_ttfr = {
    'Jira Requests': 960,
    'New Account Requests': 240
}

#change to your own slas, the number must be the minute
request_type_ttr = {
    'Jira Requests': 2400,
    'New Account Requests': 480
}

file_path = 'jira-search.xlsx'
sheet_name = 'Your Jira Issues'
data = pd.read_excel(file_path, sheet_name=sheet_name)

def elapsed_ttfr(row):
    ttfr = int(row['Time to first response (Elapsed Minutes)'])
    request_type = row['Request Type']
    request_type_hours = request_type_ttfr.get(request_type)
    if request_type_hours is not None:
        if ttfr >= 0:
            return (request_type_hours - ttfr)
        elif ttfr < 0:
            return (request_type_hours + abs(ttfr))
    else:
        if row['Issue Type'] == 'Change':
            if row['Change type'] == 'Emergency':
                if ttfr >= 0:
                    return (240 - ttfr)
                elif ttfr < 0:
                    return (240 + abs(ttfr))
            elif row['Change type'] == 'Standard':
                if ttfr >= 0:
                    return (480 - ttfr)
                elif ttfr < 0:
                    return (480 + abs(ttfr))
            elif row['Change type'] == 'Normal':
                if ttfr >= 0:
                    return (960 - ttfr)
                elif ttfr < 0:
                    return (960 + abs(ttfr))
        elif row['Issue Type'] == 'Incident':
            priority = row['Priority']
            if priority == 'Critical':
                if ttfr >= 0:
                    return (30 - ttfr)
                elif ttfr < 0:
                    return (30 + abs(ttfr))
            elif priority == 'High':
                if ttfr >= 0:
                    return (60 - ttfr)
                elif ttfr < 0:
                    return (60 + abs(ttfr))
            elif priority == 'Medium':
                if ttfr >= 0:
                    return (480 - ttfr)
                elif ttfr < 0:
                    return (480 + abs(ttfr))
            elif priority == 'Low':
                if ttfr >= 0:
                    return (960 - ttfr)
                elif ttfr < 0:
                    return (960 + abs(ttfr))

def elapsed_ttr(row):
    ttr = int(row['Time to resolution (Elapsed Minutes)'])
    request_type = row['Request Type']
    request_type_hours = request_type_ttr.get(request_type)
    if request_type_hours is not None:
        if ttr >= 0:
            return (request_type_hours - ttr)
        elif ttr < 0:
            return (request_type_hours + abs(ttr))
    else:
        if row['Issue Type'] == 'Change':
            if row['Change type'] == 'Emergency':
                if ttr >= 0:
                    return (2400 - ttr)
                elif ttr < 0:
                    return (2400 + abs(ttr))
            elif row['Change type'] == 'Standard':
                if ttr >= 0:
                    return (4800 - ttr)
                elif ttr < 0:
                    return (4800 + abs(ttr))
            elif row['Change type'] == 'Normal':
                if ttr >= 0:
                    return (7200 - ttr)
                elif ttr < 0:
                    return (7200 + abs(ttr))
        elif row['Issue Type'] == 'Incident':
            priority = row['Priority']
            if priority == 'Critical':
                if ttr >= 0:
                    return (240 - ttr)
                elif ttr < 0:
                    return (240 + abs(ttr))
            elif priority == 'High':
                if ttr >= 0:
                    return (480 - ttr)
                elif ttr < 0:
                    return (480 + abs(ttr))
            elif priority == 'Medium':
                if ttr >= 0:
                    return (2400 - ttr)
                elif ttr < 0:
                    return (2400 + abs(ttr))
            elif priority == 'Low':
                if ttr >= 0:
                    return (4800 - ttr)
                elif ttr < 0:
                    return (4800 + abs(ttr))

data['Time to first response (Elapsed Minutes)'] = data.apply(elapsed_ttfr, axis=1)
data['Time to resolution (Elapsed Minutes)'] = data.apply(elapsed_ttr, axis=1)

data.to_excel(file_path, sheet_name=sheet_name, index=False)