# HorizonTechX - Task 3: Email Address Extractor
import re

input_file = "emails.txt"
output_file = "extracted_emails.txt"

try:
    with open(input_file, "r") as file:
        text = file.read()
except FileNotFoundError:
    print(f"{input_file} not found.")
    print("Create emails.txt and add some email addresses to it.")
    raise SystemExit

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
emails = re.findall(email_pattern, text)

# Remove duplicates while keeping original order
unique_emails = list(dict.fromkeys(emails))

with open(output_file, "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

print("=== Email Extraction Complete ===")
print("Emails found:", len(unique_emails))
print("Saved to:", output_file)
