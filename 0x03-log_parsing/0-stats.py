#!/usr/bin/python3
"""
A script that reads logs from stdin, calculates metrics, and prints stats.
"""

import sys


def print_stats(total_size, status_counts):
    """Prints the current metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Main function to process log entries and calculate metrics"""
    total_size = 0
    line_count = 0
    status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            try:
                # Extract and accumulate file size
                file_size = int(parts[-1])
                total_size += file_size

                # Extract status code and update count if valid
                status_code = int(parts[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1

            except (IndexError, ValueError):
                # Skip line if it doesn't match expected format
                continue

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print stats on keyboard interruption (CTRL + C)
        print_stats(total_size, status_counts)
        raise

    # Print stats after the loop ends
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
