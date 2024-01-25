#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
import signal

# Initialize variables to store total file size and status code counts
total_size = 0
status_codes = {}
line_count = 0


# Define a function to print the statistics
def print_stats():
    global total_size, status_codes
    print("File size: {}".format(total_size))
    # Sort the status codes in ascending order and print the counts
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


# Define a signal handler to catch CTRL + C.
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Loop through the lines in stdin
for line in sys.stdin:
    # Split the line by spaces and get the status code and file size
    fields = line.split()
    try:
        status_code = int(fields[-2])
        file_size = int(fields[-1])
    except (IndexError, ValueError):
        # If the line is not in the expected format, skip it
        continue
    # Update the total file size
    total_size += file_size
    # Update the status code count or initialize it to 1 if not seen before
    status_codes[status_code] = status_codes.get(status_code, 0) + 1
    # If 10 lines have been read, print the statistics and reset the variables
    line_count += 1
    if line_count % 10 == 0:
        print_stats()
        total_size = 0
        status_codes = {}
