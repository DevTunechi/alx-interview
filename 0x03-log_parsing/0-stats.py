#!/usr/bin/python3
""" Log Parsing """
import signal
import sys


total_file_size = 0
status_code = {c: 0 for c in [
                "200", "301", "400", "401",
                "402", "403", "404", "405", "500"]}
ln_code = 0


def display_stats():
    """
        Displays the computed metrics
    """
    print("File size: {}".format(total_file_size))
    for c in sorted(status_code):
        if status_code[c] > 0:
            print("{}: {}".format(c, status_code[c]))


def keyboard_handler(sig, frame):
    """
        Handles keyboard interruption
    """
    display_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, keyboard_handler)


for ln in sys.stdin:
    try:
        blocks = ln.split()
        stats_code = blocks[-2]
        fsize = int(blocks[-1])

        total_file_size += fsize
        if stats_code in status_code:
            status_code[stats_code] += 1

        ln_code += 1
        if ln_code % 10 == 0:
            display_stats()
        except Exception:
            continue

display_stats()
