import os
import json

# Get current script directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build path to JSON
json_path = os.path.join(base_dir, "keywords.json")

# Load phishing keywords from JSON file
with open(json_path, "r") as f:
    data = json.load(f)

# Handle both dictionary and list formats
if isinstance(data, dict) and "phishing_keywords" in data:
    keywords = data["phishing_keywords"]
elif isinstance(data, list):
    keywords = data
else:
    raise ValueError("Invalid JSON format for keywords.json")

# Get user input (email or text message)
message = input("Enter the email/text message: ").lower()

# Check for keywords
found_keywords = [word for word in keywords if word in message]

if found_keywords:
    print("⚠️ Phishing Detected!")
    print("Suspicious keywords found:", ", ".join(found_keywords))
else:
    print("✅ Safe Message")
