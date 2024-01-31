Scripts that change the format of exported Jira Excel from 8h 1m to 08:01 and changes them to minutes, and calculates the elapsed time.

To use:
1. Export using Jira Excel (Not from the Export button).
2. Open and copy the values of Time to resolution and Time to first response to a new column and name them Time to resolution (Elapsed Minutes) and Time to first response (Elapsed Minutes).
3. Save file.
4. Run in this order, changeformat.py > tominutes.py > SLA.py > elapsed.py.