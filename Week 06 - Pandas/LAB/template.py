"""
RECORD CHECK  -  my version
===========================

Name  :ISHIMWE Keddy
Lane  :  IT      (delete two)
Date  :31/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).
# Question 1 - Read CSV file
import pandas as pd
df = pd.read_csv("records_sample.csv")
print(df)



# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here

df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100
    else "WARNING" if x >= 90
    else "OK"
)
print(df)


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.
# Print the full DataFrame
print(df)
not_ok = df[df["status"] != "OK"]
print(not_ok)

print(df)
status_counts = df.groupby("status").size()
print(status_counts)
df.to_csv("records_with_status.csv", index=False)
import matplotlib.pyplot as plt

status_counts.plot(kind="bar")

plt.title("Count of Records by Status")
plt.xlabel("Status")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("status_chart.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
