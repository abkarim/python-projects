import time
import string

# Time to wait in seconds
time_to_wait_in_seconds = 0.02

# Get a-z
alphabets = string.ascii_lowercase

# Get text from user
text = input("Write anything you want to animate: ")

# Remove space from beginning and end
# Convert to lowercase
text = text.strip().lower()

found = ""


for char in text:
    if char == " ":
        found += char
        continue

    for c in alphabets:
        # Wait for a while
        time.sleep(time_to_wait_in_seconds)

        print(f"{found}{c}")

        if c == char:
            found += c
            break
