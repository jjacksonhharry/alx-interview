#!/usr/bin/python3

import sys
import signal

# Dictionary to store status code counts
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Variable to store total file size
total_file_size = 0

# Function to handle keyboard interrupt (CTRL + C)
def keyboard_interrupt(signal, frame):
    print_stats()
    sys.exit(0)

# Function to print statistics
def print_stats():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

# Registering signal handler for keyboard interrupt
signal.signal(signal.SIGINT, keyboard_interrupt)

# Read stdin line by line
for i, line in enumerate(sys.stdin, start=1):
    try:
        # Split the line into components
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Increment status code count
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Add file size to total file size
        total_file_size += file_size

        # Print statistics after every 10 lines
        if i % 10 == 0:
            print_stats()

    except (ValueError, IndexError):
        # Skip the line if it doesn't match the expected format
        continue

# Print final statistics
print_stats()
