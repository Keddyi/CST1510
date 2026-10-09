"""
RECORD CHECK  -  my version
===========================

Name  :ISHIMWE keddy
Lane  :   IT      (delete two)
Date  :09/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def status_of(value, limit):
 """Determines the status by comparing the value against the limit."""
 if value > limit:
        return "OVER LIMIT"
 return "OK"

def check(value, limit):
 """Calculates and returns the difference and percentage between value and limit."""
 difference = value - limit
 percentage = (difference / limit) * 100 if limit != 0 else 0.0
 return difference, percentage

def print_report(label, value, limit, difference, percent, status):
 """Prints a neatly formatted right-aligned report inside a border."""
 border = "=" * 45
 print(border)
 print(f"| Label:      {label:<30} |")
 print(f"| Value:      {value:>30.2f} |")
 print(f"| Limit:      {limit:>30.2f} |")
 print(f"| Difference: {difference:>30.2f} |")
 print(f"| Percentage: {percent:>29.2f}% |")
 print(f"| Status:     {status:<30} |")
 print(border)



#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.
# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Enter a label (name, hostname or IP): ")     # replace with an input() call
value = float(input("Enter the value: "))     # replace with an input() call, converted
limit = float(input("Enter the limit: "))    # replace with an input() call, converted


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
difference = value-limit   # replace with your code
if limit != 0:
    percent = (difference / limit) * 100
else:
    percent = 0.0

status = status_of(value, limit)
print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)
print(f"Value:      {value:>10.2f}")
print(f"Limit:      {limit:>10.2f}")
print(f"Difference: {difference:>10.2f}")
print(f"Percentage: {percent:>9.2f}%")
print(f"Status:     {status}")
print("=" * 34)
percent = (difference / limit) * 100 # replace with your code
status = status_of(value, limit)        # replace with your code


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
