import requests

# Define the endpoint URL
endpoint = "https://nadzvkeshgazmxthgolu.supabase.co/rest/v1/demo_table?select=[id, created_at, name]"

# Set up the headers with your authentication token
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5hZHp2a2VzaGdhem14dGhnb2x1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ2MDI2MzcsImV4cCI6MjAxMDE3ODYzN30.9L3myO5HjtX77XWDCw-ESBAL1xkxjZrv9zyek4SZ8sc"
}

# Send the GET request
response = requests.get(endpoint, headers=headers)

# Check the response for success or errors
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    # Save the data to a file or process it as needed
else:
    print("Error:", response.status_code, response.text)
