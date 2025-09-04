import os
import json
import re

# -----------------------------
# Load phishing keywords
# -----------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "keywords.json")

with open(json_path, "r") as f:
    data = json.load(f)

if isinstance(data, dict) and "phishing_keywords" in data:
    keywords = data["phishing_keywords"]
elif isinstance(data, list):
    keywords = data
else:
    raise ValueError("Invalid JSON format in keywords.json")


# -----------------------------
# Function to detect fake/suspicious email IDs
# -----------------------------
def is_suspicious_email(email):
    trusted_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

    # Check valid format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True  # Invalid format

    # Extract domain
    domain = email.split("@")[-1].lower()

    # If domain not in trusted list, flag it
    if domain not in trusted_domains:
        return True

    # Check if username has too many digits
    username = email.split("@")[0]
    if sum(c.isdigit() for c in username) > 4:
        return True

    return False


# -----------------------------
# MAIN PROGRAM
# -----------------------------
message = input("Enter the email/text message: ").lower()
sender_email = input("Enter the sender's email ID: ").strip()

# Check for keywords in message
found_keywords = [word for word in keywords if word in message]

# Check if email looks suspicious
email_flagged = is_suspicious_email(sender_email)

# -----------------------------
# OUTPUT
# -----------------------------
if found_keywords or email_flagged:
    print("\n⚠️ Phishing Detected!")
    if found_keywords:
        print("Suspicious keywords found:", ", ".join(found_keywords))
    if email_flagged:
        print("Suspicious sender email:", sender_email)
else:
    print("\n✅ Safe Message & Email")
