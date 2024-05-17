# Q.2 Write a program to search for a specific pattern (e.g., email addresses or phone numbers) within a text file and extract them.

import re

def extract_emails(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails

# Example usage
file_path = 'sample.txt'
emails = extract_emails(file_path)
print("Extracted Emails:", emails)
