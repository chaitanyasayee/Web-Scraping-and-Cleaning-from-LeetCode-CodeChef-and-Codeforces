import re  # Required for pattern matching

arr = []  # Array to store the lines of the file

# Open the file
with open("cc.txt", "r") as file:
    # Read each line one by one
    for line in file:
        # Process the line
        arr.append(line.strip())  # Remove leading/trailing whitespaces and add the line to the array

def remove_elements_with_pattern(array, pattern):
    new_array = []
    for element in array:
        if pattern not in element:
            new_array.append(element)
        else:
            print("Removed: " + element)
    return new_array

# Remove lines containing "/solution"
arr = remove_elements_with_pattern(arr, "/solution")

# Clean the URLs
cleaned_urls = []
for url in arr:
    # Extract the problem code from the URL using regular expression
    match = re.search(r'\/problems\/([A-Za-z0-9_]+)$', url)
    if match:
        problem_code = match.group(1)
        # Check if the problem code ends with a number greater than 1
        if re.search(r'[2-9]$', problem_code):
            continue  # Skip the current URL if it ends with a number greater than 1
        cleaned_urls.append(f"https://www.codechef.com/problems/{problem_code}")

with open('cc_problems.txt', 'a') as f:
    # Iterate over each URL in the cleaned list
    for url in cleaned_urls:
        # Write each URL to the file, followed by a newline
        f.write(url + "\n")
