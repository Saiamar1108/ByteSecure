import json

# Load phishing keywords from JSON file
with open("keywords.json", "r") as f:
    data = json.load(f)

keywords = data["phishing_keywords"]

# Get user input (email or text message)
message = input("Enter the email/text message: ").lower()

# Check for keywords
found_keywords = [word for word in keywords if word in message]

if found_keywords:
    print("⚠️ Phishing Detected!")
    print("Suspicious keywords found:", ", ".join(found_keywords))
else:
    print("✅ Safe Message")
# Save the result to a log file
with open("detection_log.txt", "a") as log_file:   
    if found_keywords:
        log_file.write(f"Phishing Detected: {', '.join(found_keywords)} in message: {message}\n")
    else:
        log_file.write(f"Safe Message: {message}\n")
        