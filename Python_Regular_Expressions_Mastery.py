# Task 1: Name Verification

import re # importing regex

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]
def correct_name_format(names):
    for name in names:
        if re.match(r"[A-Z]\w+\s|[A-Z]\s[A-Z]\w+", name): # Using the re.match() method to obtain the information we need. The pattern we used checks to see if the first character in the first name is a capital letter (A-Z); then checks to see if there are other word characters following it; then looks to see if there is any whitespace; it then comes to an or block (|) to see if the next character will be another capital letter instead; followed by looking for whitespace; it then checks for any word characters following the capital letter.
            print(name) # Prints the name if it meets the re.match() method requirements.
        else:
            print("Invalid name") # Prints this string if the name does not meet the re.match() method requirements.
correct_name_format(names) # Calling our function.