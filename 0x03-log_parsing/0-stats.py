#!/usr/bin/python3

import sys

def parseLogs():
    """
    Reads logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

    try:
        for line in sys.stdin:
            lineNumber += 1
            elements = line.strip().split()
            try:
                fileSize += int(elements[-1])
                if elements[-2] in codes:
                    statusCodes[elements[-2]] = statusCodes.get(elements[-2], 0) + 1
            except (IndexError, ValueError):
                pass

            if lineNumber % 10 == 0:
                report(fileSize, statusCodes)

        report(fileSize, statusCodes)
    except KeyboardInterrupt:
        report(fileSize, statusCodes)
        raise

def report(fileSize, statusCodes):
    """
    Prints generated report to standard output
    Args:
        fileSize (int): total log size after every 10 successfully read line
        statusCodes (dict): dictionary of status codes and counts
    """
    print("File size:", fileSize)
    for key in sorted(statusCodes):
        print(key + ":", statusCodes[key])

if __name__ == '__main__':
    parseLogs()

