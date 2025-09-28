# Problem-1: Docker Log Analyzer
# Build a script that reads a Docker log file and returns error messages with timestamps.
# -   **Hint**: Look for keywords like `"ERROR"` or `"Exception"` using regex.

import re


def extract_error_logs_from_string(log_content):
    error_logs = []
    error_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*(ERROR|Exception).*', re.IGNORECASE)

    for line in log_content.splitlines():
        if not line.strip():
            continue
            
        match = error_pattern.search(line)
        if match:
            timestamp = match.group(1) 
            error_message = line.strip() 
            error_logs.append((timestamp, error_message))
    
    return error_logs

log_content = """
2023-10-26 09:00:01 INFO: Application started.
2023-10-26 09:01:15 ERROR: Disk space low.
2023-10-26 09:02:30 DEBUG: Processing task 101.
2023-10-26 09:03:45 WARNING: High memory usage.
2023-10-26 09:04:59 EXCEPTION: NullPointerException at line 45.
2023-10-26 09:05:00 error: Another type of error message.
2023-10-26 09:06:01 Info: Final process finished.
"""

# Call the new function with the string content
result = extract_error_logs_from_string(log_content)
print("--- Extracted Error Logs ---")
for ts, msg in result:
    print(f"[{ts}] {msg}")