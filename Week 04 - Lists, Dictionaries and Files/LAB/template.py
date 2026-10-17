"""
RECORD CHECK  -  my version
===========================

Name  :ISHIMWE Keddy
Lane  :  IT      (delete two)
Date  :17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Calculate the difference, percentage difference, and status of a record."""
    difference = value - limit

    if limit != 0:
        percent = (difference / limit) * 100
    else:
        percent = 0

    if difference > 0:
        status = "Above limit"
    elif difference < 0:
        status = "Below limit"
    else:
        status = "Within limit"

    return difference, percent, status


def print_report(value, limit):
    """Print a report showing the value, limit, difference, percentage, and status."""
    difference, percent, status = check_record(value, limit)

    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference}")
    print(f"Percentage difference: {percent:.2f}%")
    print(f"Status: {status}")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
import os

def load_records(path):
    """Load records from a file into a list of dictionaries."""
    records = []

    file_path = os.path.join(os.path.dirname(__file__), path)

    with open(file_path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records




records = load_records("records.txt")

for record in records:
    print(record["label"])
    print_report(record["value"], record["limit"])

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_limit_count = 0

for record in records:
    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"]
    )

    if status == "Above limit":
        over_limit_count += 1

print(f"Total records over limit: {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
