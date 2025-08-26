import matplotlib.pyplot as plt
import requests
import json

# URL to request data from
url = 'https://api.webtigerpython.ethz.ch/librariescount'


try:
    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data (assuming it's in JSON format)
        data = response.json()  # Use response.text for plain text or HTML
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
# Initialize variables for grouping
grouped_count = 0
grouped_label = 'Others'
final_data = []

total_count = sum(item[1] for item in data)


# Process the data
for library, count in data:
    if count < 1000:
        grouped_count += count
    else:
        final_data.append([library, count])

final_data.append([grouped_label, grouped_count])

# Extract counts and library names
counts = [item[1] for item in final_data]
library_names = [item[0] for item in final_data]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=library_names, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set1.colors, textprops={'fontsize': 15, 'color': 'white'})
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.text(0, -1.2, f'Total Count: {total_count} Collected over approx 3 months', ha='center', fontsize=12, color='white')
plt.title('Error Reports by Library', fontsize=25, pad=20, color='white') 


# Show the plot
plt.savefig("wtp_error_reports", transparent=True)
